import math
import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities


def main():
    # Windows system-volume interface (supported by current Pycaw versions).
    speakers = AudioUtilities.GetSpeakers()
    volume = speakers.EndpointVolume
    min_volume, max_volume, _ = volume.GetVolumeRange()

    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        model_complexity=0,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7,
    )

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Could not open the webcam. Close other camera apps or try camera index 1.")
        hands.close()
        return

    try:
        while True:
            success, frame = camera.read()
            if not success:
                print("Could not read a frame from the webcam.")
                break

            frame = cv2.flip(frame, 1)
            height, width, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb_frame)

            if result.multi_hand_landmarks:
                hand_landmarks = result.multi_hand_landmarks[0]
                mp_draw.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

                thumb = hand_landmarks.landmark[4]
                index = hand_landmarks.landmark[8]
                x1, y1 = int(thumb.x * width), int(thumb.y * height)
                x2, y2 = int(index.x * width), int(index.y * height)

                distance = math.hypot(x2 - x1, y2 - y1)

                # Tune these values for your camera/hand distance if needed.
                volume_percent = float(np.interp(distance, [20, 200], [0, 100]))
                volume_percent = float(np.clip(volume_percent, 0, 100))
                target_db = float(
                    np.interp(volume_percent, [0, 100], [min_volume, max_volume])
                )
                volume.SetMasterVolumeLevel(target_db, None)

                cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
                cv2.circle(frame, (x1, y1), 8, (255, 0, 255), cv2.FILLED)
                cv2.circle(frame, (x2, y2), 8, (255, 0, 255), cv2.FILLED)
                cv2.putText(
                    frame,
                    f"Volume: {int(volume_percent)}%",
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )
            else:
                cv2.putText(
                    frame,
                    "Show one hand to the camera",
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2,
                )

            cv2.imshow("Hand Gesture Volume Control - Press Q to quit", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        hands.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
