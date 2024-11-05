import serial.tools.list_ports
from ultralytics import YOLO
import cv2 as cv
import cvzone
import math
import time
import random

# Listing all ports
ports = serial.tools.list_ports.comports()
portsList = []
for port in ports:
    portsList.append(str(port))
    print(str(port))

# Initializing Com Port
com = input("Select Com Port for Arduino #: ")
for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
serialInstance = serial.Serial()
serialInstance.baudrate = 115200
serialInstance.port = use
serialInstance.open()
time.sleep(5)
print("Using COM" + str(com))

# Make YOLO Model
model = YOLO("models/yolov8n.pt")

# YOLO v8 class names list
classNames = [
    "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
    "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
    "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
    "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
    "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
    "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
    "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
    "teddy bear", "hair drier", "toothbrush"
]

# Congestion Photos List
congestion_list = [
    "images/Congestion 4.jpeg", 
    "images/Congestion 6.jpeg", 
    "images/Congestion 9.jpeg", 
    "images/Congestion 10.jpeg",
    "images/Congestion 1.jpeg", 
]

# Turning on red light as the initial condition
print("Setting up traffic light!")
serialInstance.write("0red".encode('utf-8'))
time.sleep(3)
serialInstance.write("1red".encode('utf-8'))
print("Turning all traffic lights to red for ~5 seconds")
time.sleep(5)

# Define a function to categorize vehicles
def isVehicle(name):
    return name in ["bicycle", "car", "motorbike", "bus", "truck"]

# Define openCV rescale function
def rescaleFrame(frame, scale):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

curidx = 0
while True:
    print(f"It's the traffic light with index {curidx} turn!")
    # Choose a random congestion photo, rescale, then show
    congestion = random.choice(congestion_list)
    img = cv.imread(congestion)
    print(f"Reading {congestion}")
    img = rescaleFrame(img, 0.25)
    # cv.imshow(congestion.split('/')[1], img)

    # Detecting vehicles and count them
    results = model(img, stream=True)
    vehicles = 0
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls = int(box.cls[0])
            if not isVehicle(classNames[cls]):
                continue
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2, = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            conf = math.ceil(box.conf[0] *100) / 100
            if conf > 0.25:
                vehicles += 1
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(30, y1)), scale=1, thickness=1)
    # cv.imshow("Vehicles Detection", img)

    # Blink yellow light
    serialInstance.write(f"{curidx}yellow".encode('utf-8'))
    time.sleep(2)
    print(f"{vehicles} vehicles are detected")

    # Turn on green light based on the number of vehicles detected
    green_light = vehicles * 1.5
    serialInstance.write(f"{curidx}green".encode('utf-8'))
    print(f"Turning green light for {green_light} seconds in traffic light {curidx}")
    time.sleep(green_light)

    serialInstance.write(f"{curidx}yellow".encode('utf-8'))
    time.sleep(2)
    print(f"{vehicles} vehicles are detected")

    serialInstance.write(f"{curidx}red".encode('utf-8'))
    print(f"Turn back traffic light {curidx} to become red")
    time.sleep(2)

    curidx = (curidx + 1) % 2
