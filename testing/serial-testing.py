import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()
serialInstance = serial.Serial()
portsList = []

for port in ports:
    portsList.append(str(port))
    print(str(port))

com = input("Select Com Port for Arduino #: ")

for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)

serialInstance.baudrate = 115200
serialInstance.port = use
serialInstance.open()
time.sleep(5)
print("Using COM" + str(com))

while True:
    command = input("Arduino Command: ")
    serialInstance.write(command.encode('utf-8'))
    if command == "exit":
        exit()