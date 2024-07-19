# Kinect Hand Tracking

A Python project that uses Azure Kinect DK for hand tracking and controlling the mouse with gestures.

## Description

This repository contains a Python script that leverages the Azure Kinect DK camera, MediaPipe for hand tracking, and PyAutoGUI for controlling the mouse cursor through hand gestures. The project captures video frames from the Kinect camera, processes the frames to detect hand landmarks, and moves the mouse cursor based on the position of the index finger. Additionally, it allows clicking based on the proximity of the thumb and index finger.

## Features

- Capture video frames from the Azure Kinect DK camera.
- Detect hand landmarks using MediaPipe.
- Control the mouse cursor with the index finger.
- Perform mouse clicks by pinching (bringing the thumb and index finger together).

## Requirements

- Python 3.7 or higher
- Azure Kinect DK
- Azure Kinect SDK and dependencies
- Microsoft Visual C++ Build Tools
- OpenCV
- MediaPipe
- PyAutoGUI
- PyK4A

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/YOUR_USERNAME/kinect-hand-tracking.git
    cd kinect-hand-tracking
    ```

2. **Install Microsoft Visual C++ Build Tools:**

    - Download and install [Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

3. **Install the required Python packages:**

    ```sh
    pip install opencv-python mediapipe pyautogui pyk4a
    ```

4. **Install Azure Kinect SDK:**
   
   Follow the instructions for your operating system on the [Azure Kinect SDK](https://docs.microsoft.com/en-us/azure/kinect-dk/sdk-download) download page.

## Usage

1. **Connect your Azure Kinect DK camera to your computer.**

2. **Run the script:**

    ```sh
    python kinect_hand_tracking.py
    ```

3. **Control the mouse:**

    - Move your hand in front of the camera to see the hand landmarks.
    - Use your index finger to move the mouse cursor.
    - Bring your thumb and index finger together to perform a mouse click.
