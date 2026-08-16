# 🔊 Virtual Volume Control

Control your computer's **system volume using hand gestures** through a webcam.

This project uses computer vision to track the hand and interprets the distance between selected fingers as a volume-control input. The closer or farther the fingers are, the system adjusts the speaker volume accordingly.

## 🎯 Project Idea

The goal is to create a **touch-free volume controller** that replaces traditional keyboard shortcuts or manual volume controls with a simple hand gesture.

## 🌟 Features

* 🎥 Real-time webcam interaction
* 🖐️ Hand gesture tracking
* 🔊 Live system volume adjustment
* 📏 Finger-distance based volume control
* ⚡ Real-time response
* 💻 Works with the computer's audio output

## 🔄 Working Pipeline

```text
Webcam
   ↓
Capture Hand
   ↓
Detect Hand Landmarks
   ↓
Track Finger Positions
   ↓
Calculate Finger Distance
   ↓
Map Distance to Volume Level
   ↓
Adjust System Volume
```

## 🧠 How It Works

The webcam captures the user's hand continuously.

Computer vision detects the hand landmarks and identifies the required finger positions.

The distance between the selected fingers is calculated and converted into a volume level.

```text
Small Finger Distance  →  Lower Volume

Large Finger Distance  →  Higher Volume
```

This allows the user to increase or decrease the system volume naturally by moving their fingers.

## 🛠️ Technologies

| Technology | Role                          |
| ---------- | ----------------------------- |
| Python     | Main programming language     |
| OpenCV     | Webcam and image processing   |
| MediaPipe  | Hand landmark tracking        |
| Pycaw      | Windows system volume control |

## 📦 Installation

Install the required Python libraries:

```bash
pip install opencv-python mediapipe pycaw
```

## ▶️ Run

Open the project directory and run:

```bash
python app.py
```

Make sure your webcam is available and allow camera access when requested.

## 🎮 Gesture Control

| Hand Movement         | Volume      |
| --------------------- | ----------- |
| Fingers closer        | 🔉 Decrease |
| Fingers farther apart | 🔊 Increase |

The volume changes continuously according to the detected finger distance.

## 📁 Project Structure

```text
virtual-volume-control/
│
├── app.py
└── README.md
```

## 💡 Applications

This project demonstrates how hand gestures can be used for:

* Touch-free media control
* Smart computer interfaces
* Accessibility solutions
* Human-Computer Interaction
* Computer Vision applications
* AI project demonstrations

## 🚀 Future Enhancements

Possible improvements include:

* 🎵 Gesture-based media play/pause
* ⏭️ Next and previous track control
* 🔇 Mute/unmute gesture
* 🖐️ Multi-hand controls
* 🎚️ Improved volume smoothing
* 🖥️ On-screen volume indicator

## 👨‍💻 Developer

**Sagar Dhodi**

AI & Computer Vision Project

---

⭐ **If you find this project useful, consider starring the repository.**
