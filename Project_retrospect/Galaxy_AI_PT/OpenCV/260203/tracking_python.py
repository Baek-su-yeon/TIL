import cv2
import time
import json
import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from configs.settings import POSE_MODEL

# 1. 전역 변수 및 결과 저장소
latest_pose_landmarks = None
prev_data = {"e": None, "s": None, "t": None, "time": 0}
speeds = {"e": 0.0, "s": 0.0, "t": 0.0}
last_send_time = 0  # 10Hz 제어용 타이머

def calculate_center_all(landmarks, indices):
    """지정한 인덱스들의 중심 좌표 반환 (가시성 상관없이 좌표 계산)"""
    if not landmarks: return 0.0, 0.0
    
    target_points = [landmarks[i] for i in indices]

    # 가시성(Visibility) 평균 계산
    avg_vis = sum([p.visibility for p in target_points]) / len(target_points)

    if avg_vis <= 0.6:
        return None, None, 0.0
    
    avg_x = sum([p.x for p in target_points]) / len(target_points)
    avg_y = sum([p.y for p in target_points]) / len(target_points)

    return avg_x, avg_y, avg_vis

def calculate_speed(p1, p2, dt):
    """두 점 사이의 유클리드 거리 / 시간차 = 속도 (정규화 좌표 기준)"""
    if p1 is None or p2 is None or dt <= 0: return 0.0
    dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    return dist / dt

# 2. 비동기 콜백 함수
def pose_callback(result: vision.PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    global latest_pose_landmarks
    if result.pose_landmarks:
        latest_pose_landmarks = result.pose_landmarks[0]

# 3. Pose Landmarker 설정
base_options = mp.tasks.BaseOptions
pose_options = vision.PoseLandmarkerOptions(
    base_options=base_options(
        model_asset_path= POSE_MODEL,
        delegate=python.BaseOptions.Delegate.GPU
    ),
    running_mode=vision.RunningMode.LIVE_STREAM,
    result_callback=pose_callback
)

pose_landmarker = vision.PoseLandmarker.create_from_options(pose_options)
cap = cv2.VideoCapture(0)

print("--- Multi-Point Tracking Started ---")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    h, w, _ = frame.shape
    curr_time = time.time()
    dt = curr_time - prev_data["time"] if prev_data["time"] != 0 else 0.033
    # 프레임 간 시간 업데이트는 매 루프마다 수행
    prev_data["time"] = curr_time

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    pose_landmarker.detect_async(mp_image, int(curr_time * 1000))

    if latest_pose_landmarks:
        # 1. 각 부위별 데이터 계산을 위한 정의
        parts_config = {
            "e": [2, 5],            # Eyes
            "s": [11, 12],          # Shoulders
            # "t": [11, 12, 23, 24]   # Torso
        }
        
        current_pixels = {} # 현재 프레임의 픽셀 좌표 저장용

        for key, indices in parts_config.items():
            nx, ny, vis = calculate_center_all(latest_pose_landmarks, indices)
            
            if vis > 0.6:
                current_pixels[key] = (nx, ny)
                speeds[key] = calculate_speed(prev_data[key], (nx, ny), dt)
                prev_data[key] = (nx, ny)
            else:
                current_pixels[key] = None
                speeds[key] = 0.0
                prev_data[key] = None

        # 2. 방향 판정 로직 (안전하게 처리)
        # 값이 있는 부위들만 추출해서 판정
        valid_x_coords = [pos[0] for pos in current_pixels.values() if pos is not None]
        
        direction = "CENTER"
        w_1_3, w_2_3 = 0.33, 0.66

        if valid_x_coords:
            if any(x < w_1_3 for x in valid_x_coords):
                direction = "RIGHT" # 전면 카메라 기준
            elif any(x > w_2_3 for x in valid_x_coords):
                direction = "LEFT"

        # 보내는 속도 계산
        # 10Hz = 1 / 10 = 0.1 / 20Hz = 1 / 20 = 0.05
        if direction != "CENTER" and (curr_time - last_send_time) >= 0.1:
            last_send_time = curr_time

            # 3. JSON 출력 (데이터가 정갈하도록 int 변환)
            output = {"dir": direction}
            for key in ["e", "s"]:
                pos = current_pixels[key]
                output.update({
                    f"{key}x": int(pos[0] * 1000) if pos else 0,
                    f"{key}y": int(pos[1] * 1000) if pos else 0,
                    f"{key}v": int(speeds[key] * 1000)
                })
            print(json.dumps(output), flush=True)

        # 4. 시각화 (가이드라인 및 포인트)
        cv2.line(frame, (int(w_1_3 * w), 0), (int(w_1_3 * w), h), (200, 200, 200), 1)
        cv2.line(frame, (int(w_2_3 * w), 0), (int(w_2_3 * w), h), (200, 200, 200), 1)

        colors = {"e": (255, 0, 0), "s": (0, 255, 0)}
        for i, (key, pos) in enumerate(current_pixels.items()):
            if pos:
                cv2.circle(frame, (int(pos[0] * w), int(pos[1] * h)), 8, colors[key], -1)
                cv2.putText(frame, f"{key.upper()}_Vel: {int(speeds[key])}", 
                            (10, 30 + i*20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[key], 1)

        # 상태 출력
        color = (0, 0, 255) if direction != "CENTER" else (0, 255, 0)
        cv2.putText(frame, f"DIR: {direction}", (w // 2 - 70, 50), 
                    cv2.FONT_HERSHEY_DUPLEX, 1.2, color, 2)

    cv2.imshow('Multi-Point Redundant Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

pose_landmarker.close()
cap.release()
cv2.destroyAllWindows()