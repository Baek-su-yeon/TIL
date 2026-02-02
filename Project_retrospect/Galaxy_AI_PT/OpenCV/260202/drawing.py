import cv2
import time
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# 기존 설정들 (HAND_MODEL 등은 사용자 환경에 맞춰 설정되어 있다고 가정)
from configs.settings import HAND_MODEL
# from src.utils.utils import PerformanceMonitor
# from .gesture_python import GestureRecognizer

# 테스트를 위한 임시 경로 (실제 경로로 수정 필요)
# HAND_MODEL = "gesture_recognizer.task" 

# --- [추가] 그리기 관련 변수 ---
drawing_canvas = None
prev_pos = {"Left": None, "Right": None}
draw_color = (255, 0, 255) # 보라색 펜
thickness = 5
# ---------------------------

latest_hand_results = {"Left": "None", "Right": "None"}
latest_hand_raw_labels = {}
latest_hand_landmarks_dict = {"Left": None, "Right": None}
request_start_times = {}

def gesture_callback(result: vision.GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    global latest_hand_results, latest_hand_raw_labels, latest_hand_landmarks_dict
    
    temp_labels = {}
    display_results = {"Left": "None", "Right": "None"}
    temp_landmarks = {"Left": None, "Right": None}

    if result.gestures and result.handedness:
        for i in range(len(result.gestures)):
            gesture = result.gestures[i][0]
            gesture_label = gesture.category_name
            hand_label = result.handedness[i][0].category_name 
            
            display_results[hand_label] = f"{gesture_label} ({gesture.score:.2f})"
            temp_labels[hand_label] = gesture_label
            temp_landmarks[hand_label] = result.hand_landmarks[i]

    latest_hand_results = display_results
    latest_hand_raw_labels = temp_labels
    latest_hand_landmarks_dict = temp_landmarks

# 모델 설정
base_options = mp.tasks.BaseOptions
hand_gesture_options = vision.GestureRecognizerOptions(
    base_options=base_options(model_asset_path=HAND_MODEL),
    running_mode=vision.RunningMode.LIVE_STREAM,
    num_hands=2,
    min_hand_detection_confidence=0.7,
    result_callback=gesture_callback
)

hand_gesture = vision.GestureRecognizer.create_from_options(hand_gesture_options)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    
    frame = cv2.flip(frame, 1) # 좌우 반전 (거울 모드, 그리기 편함)
    h, w, _ = frame.shape

    # --- [추가] 캔버스 초기화 (최초 1회) ---
    if drawing_canvas is None:
        drawing_canvas = np.zeros((h, w, 3), dtype=np.uint8)
    # -----------------------------------

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    timestamp_ms = int(time.time() * 1000)
    request_start_times[timestamp_ms] = timestamp_ms
    hand_gesture.recognize_async(mp_image, timestamp_ms)

    # --- [수정] 그리기 로직 구현 ---
    for side in ["Left", "Right"]:
        label = latest_hand_raw_labels.get(side)
        landmarks = latest_hand_landmarks_dict.get(side)

        if label == "Pointing_Up" and landmarks:
            # 검지 손가락 끝 번호는 8번입니다.
            idx_finger = landmarks[8]
            curr_x, curr_y = int(idx_finger.x * w), int(idx_finger.y * h)

            if prev_pos[side] is not None:
                # 이전 좌표가 있으면 선을 긋습니다.
                cv2.line(drawing_canvas, prev_pos[side], (curr_x, curr_y), draw_color, thickness)
            
            prev_pos[side] = (curr_x, curr_y) # 현재 좌표 업데이트
        else:
            # 제스처가 바뀌거나 손이 없으면 이전 좌표 초기화 (선 끊기)
            prev_pos[side] = None

    # --- [추가] 합성 및 화면 표시 ---
    # 캔버스에서 그림이 있는 부분만 원본 프레임에 덧씌움
    img_gray = cv2.cvtColor(drawing_canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 20, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    
    # 원본에서 그림 부분을 제외하고 추출 + 캔버스의 그림 부분 추출
    frame = cv2.bitwise_and(frame, img_inv)
    frame = cv2.bitwise_or(frame, drawing_canvas)

    # UI 정보 표시
    cv2.putText(frame, "C: Clear | Q: Quit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"L: {latest_hand_results['Left']}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv2.putText(frame, f"R: {latest_hand_results['Right']}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow('Air Drawing Test', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'): # C 누르면 그림 초기화
        drawing_canvas = np.zeros((h, w, 3), dtype=np.uint8)

hand_gesture.close()
cap.release()
cv2.destroyAllWindows()