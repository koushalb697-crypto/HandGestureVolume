# Hand Gesture Volume Control

Control your Windows laptop's master volume using hand gestures detected by your webcam.

The application uses **Python**, **OpenCV**, and **MediaPipe** to track the distance between your thumb and index finger. It maps that distance to the Windows system volume using **Pycaw**.

## Features

- Real-time webcam hand tracking
- Thumb–index finger distance controls volume
- Displays the volume percentage on the camera window
- Press `Q` to quit

## Demo

Add a screenshot or GIF of your project here after running it:

```markdown
![Hand Gesture Volume Control demo](assets/demo.gif)
```

## Requirements

- Windows 10 or Windows 11
- Python **3.12** (recommended for the dependency versions in this project)
- A working webcam
- Microphone/camera permission is not needed; allow **Camera** access if Windows asks

> Pycaw controls Windows audio. This project is not intended for macOS or Linux without replacing the volume-control implementation.

## Installation

### 1. Clone the repository

Replace `YOUR-USERNAME` with your GitHub username:

```bash
git clone https://github.com/YOUR-USERNAME/HandGestureVolume.git
cd HandGestureVolume
```

Or download the repository ZIP from GitHub and extract it.

### 2. Create and activate a virtual environment

```cmd
py -3.12 -m venv .venv
.venv\Scripts\activate
```

If `py -3.12` is not recognized, install Python 3.12 from the official Python website and reopen Command Prompt.

### 3. Install dependencies

```cmd
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the application

```cmd
python hand_volume.py
```

A webcam window should appear. Show one hand to the camera:

- Move your thumb and index finger **apart** to increase volume.
- Bring them **closer together** to decrease volume.
- Press **Q** to close the application.

## Troubleshooting

### `ModuleNotFoundError`
Make sure the virtual environment is activated and install dependencies again:

```cmd
python -m pip install -r requirements.txt
```

### `mediapipe has no attribute 'solutions'`
This project uses the legacy MediaPipe Hands API. Confirm that the installed version is `0.10.21`:

```cmd
python -c "import mediapipe as mp; print(mp.__version__); print(hasattr(mp, 'solutions'))"
```

Expected output includes `0.10.21` and `True`. Use Python 3.12 if the package cannot be installed for your Python version.

### Webcam does not open
Close other apps that may be using the camera. You can also change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` in `hand_volume.py` if your webcam uses another device index.

### Volume changes too quickly
Lighting, camera position, and hand movement can affect tracking. Keep your hand in view and adjust the distance range in the code if needed.

## How it works

1. OpenCV captures frames from the webcam.
2. MediaPipe detects hand landmarks.
3. The program measures the distance between landmark 4 (thumb tip) and landmark 8 (index fingertip).
4. NumPy maps that distance to a 0–100% volume range.
5. Pycaw updates the Windows master volume.

## Project structure

```text
HandGestureVolume/
├── hand_volume.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## Future improvements

- Add a mute/unmute gesture
- Smooth volume changes to reduce jitter
- Add a start/stop button and graphical interface
- Support multiple gestures and configurable sensitivity

## License

This project is licensed under the MIT License. See `LICENSE`.
