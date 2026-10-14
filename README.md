# Hand Gesture Volume Control 🖐️🔊

Control your Windows laptop's master volume using hand gestures detected by your webcam.

This personal project uses **Python**, **OpenCV**, and **MediaPipe** to track the distance between your thumb and index finger, then maps that distance to the Windows system volume using **Pycaw**.

## Demo

🎥 **Watch the demo video on LinkedIn:** [https://www.linkedin.com/posts/koushal-b-koush_opencv-computervision-python-activity-7514400563351109633-megT?utm_source=li_share&utm_content=feedcontent&utm_medium=g_dt_web&utm_campaign=copy]
## Features

- Real-time webcam hand tracking
- Thumb–index finger distance controls volume
- Displays the volume percentage in the camera window
- Press `Q` to quit the application

## Technologies Used

- Python 3.12
- OpenCV
- MediaPipe
- NumPy
- Pycaw
- comtypes

## Requirements

- Windows 10 or Windows 11
- Python 3.12 (recommended for the dependency versions used here)
- A working webcam

> **Platform note:** Pycaw controls Windows audio. This project will not control system volume on macOS or Linux without a different audio-control implementation.

## Installation and Setup

### 1. Download or clone this repository

```bash
git clone https://github.com/koushalb697-crypto/HandGestureVolume
cd HandGestureVolume
```
### 2. Create a virtual environment

On Windows Command Prompt:

```cmd
py -3.12 -m venv .venv
.venv\Scripts\activate
```

If `py -3.12` is not recognized, install Python 3.12 from the [official Python downloads page](https://www.python.org/downloads/windows/), then reopen Command Prompt.

### 3. Install the dependencies

```cmd
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the application

```cmd
python hand_volume.py
```

Allow camera access if Windows asks. Show one hand to the webcam:

- Move your thumb and index finger **apart** to increase the volume.
- Bring them **closer together** to decrease the volume.
- Press **Q** to close the application.

## How It Works

1. OpenCV captures video frames from the webcam.
2. MediaPipe detects hand landmarks.
3. The program measures the distance between landmark 4 (thumb tip) and landmark 8 (index fingertip).
4. NumPy maps the distance to a 0–100% volume range.
5. Pycaw updates the Windows master volume.

## Project Structure

```text
HandGestureVolume/
├── hand_volume.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
└── Demo/                     
    └── HandGestureVolumeDemo.mp4
```

## Troubleshooting

### `ModuleNotFoundError`

Activate your virtual environment and install the dependencies:

```cmd
python -m pip install -r requirements.txt
```

### `mediapipe has no attribute 'solutions'`

This project uses the MediaPipe Hands API available in the pinned version. Check your installation:

```cmd
python -c "import mediapipe as mp; print(mp.__version__); print(hasattr(mp, 'solutions'))"
```

The expected version is `0.10.21`, and the second output should be `True`. If installation fails under your current Python version, use Python 3.12 and recreate the virtual environment.

### Webcam does not open

Close other applications that might be using the camera. If necessary, change `cv2.VideoCapture(0)` in `hand_volume.py` to `cv2.VideoCapture(1)` and try again.

### Volume changes too quickly

Hand distance can vary with camera position and movement. Keep your hand visible and adjust the distance range in the code if needed.

## Future Improvements

- Add a mute/unmute gesture
- Smooth volume changes to reduce jitter
- Add a graphical interface with start/stop controls
- Add adjustable sensitivity and support for more gestures

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
