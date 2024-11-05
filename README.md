# 🚦 AI-Driven Traffic Lights with Computer Vision (Beta Version)

Welcome to the beta version of the **AI-driven Traffic Lights with Computer Vision** project! Our aim is to help reduce traffic congestion by dynamically adjusting red and green light durations based on real-time vehicle detection.

## 🔍 How Does It Work?

This project combines the **YOLOv8 model** (from the Ultralytics library) with **OpenCV** to detect and count vehicles approaching the intersection. Using this data, the system adjusts the traffic light duration to allow more vehicles to pass during busy times and reduce unnecessary waiting during quiet periods.

The setup also includes **Arduino UNO** for prototyping, allowing seamless control over the lights based on vehicle count. Check out the full circuit schema below to try it yourself!

## 🛠️ Getting Started

Here’s a quick guide to help you set up and test the project.

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repo/ai-driven-traffic-lights.git
   cd ai-driven-traffic-lights
2. **Install Dependencies**

   This project requires Python libraries such as `Ultralytics` and `OpenCV`. Install them with:
   
   ```bash
   pip install ultralytics opencv-python
4. **Setup the Arduino**
   
   Connect your Arduino UNO as shown in the circuit schema below, then upload the provided Arduino code to get started.

6. **Run the Program**
   
   With everything connected, run the script:
   
   ```bash
   python main.py

Watch as the traffic light changes duration based on real-time vehicle detection!

## 🖥️ Tech Stack

- **YOLOv8**: For vehicle detection and counting.
- **OpenCV**: For image processing and video feed handling.
- **Arduino UNO**: To control the physical traffic light prototype.

## 🗺️ Circuit Schema

_(Refer to the diagram below for your connections)_
![Circuit_Schema](https://github.com/user-attachments/assets/d42fdcd9-b34d-4064-999e-f0f7e0410244)

## 📌 Next Steps

- **Testing & Optimization**: This beta version is the foundation. Fine-tuning the model and experimenting with different thresholds will further improve traffic efficiency.
- **Feedback**: Your feedback is essential! Try it out, report any issues, or suggest improvements.

## 🤝 Contributing

Interested in contributing? Please feel free to fork this repo, make improvements, and submit a pull request. Let’s work together to make traffic flow smoother for everyone!
