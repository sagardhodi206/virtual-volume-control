import cv2
import mediapipe as mp
import math
import numpy as np

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# ==========================
# Audio Setup
# ==========================
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_,
    CLSCTX_ALL,
    None
)

volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]

# ==========================
# Camera
# ==========================
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# ==========================
# MediaPipe
# ==========================
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mpDraw = mp.solutions.drawing_utils

# ==========================
# Main Loop
# ==========================
while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            mpDraw.draw_landmarks(
                img,
                handLms,
                mpHands.HAND_CONNECTIONS
            )

            h, w, c = img.shape

            # Thumb Tip
            x1 = int(handLms.landmark[4].x * w)
            y1 = int(handLms.landmark[4].y * h)

            # Index Tip
            x2 = int(handLms.landmark[8].x * w)
            y2 = int(handLms.landmark[8].y * h)

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            cv2.circle(img, (x1, y1), 12, (255, 0, 255), -1)
            cv2.circle(img, (x2, y2), 12, (255, 0, 255), -1)

            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            cv2.circle(img, (cx, cy), 10, (0, 255, 0), -1)

            # Distance
            length = math.hypot(x2 - x1, y2 - y1)

            # Convert distance to volume
            vol = np.interp(length, [30, 250], [minVol, maxVol])
            volBar = np.interp(length, [30, 250], [400, 150])
            volPer = np.interp(length, [30, 250], [0, 100])

            volume.SetMasterVolumeLevel(vol, None)

            if length < 30:
                cv2.circle(img, (cx, cy), 12, (0, 0, 255), -1)

            # Volume Bar
            cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)

            cv2.rectangle(
                img,
                (50, int(volBar)),
                (85, 400),
                (255, 0, 0),
                -1
            )

            cv2.putText(
                img,
                f'{int(volPer)} %',
                (35, 440),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )

    cv2.putText(
        img,
        "Virtual Volume Control",
        (350, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Virtual Volume Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()