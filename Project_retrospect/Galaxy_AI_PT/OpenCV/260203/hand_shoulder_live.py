# 추론 및 시각화 관련
import cv2
import time
import mediapipe as mp
from mediapipe.tasks import python # modelpipe python 쑬 때
from mediapipe.tasks.python import vision # modelpipe 중 vision 작업할 때
from configs.settings import HAND_MODEL, POSE_MODEL, HAND_ORIGIN_MODEL
from src.utils.utils import PerformanceMonitor

# ID 출력 테스트용
import collections
from .gesture_python import GestureRecognizer

# 전역 변수
# 비동기 처리의 지연 시간 계산을 위한 타임스탬프 맵
# {timestamp_ms: start_time_ms} 형태로 저장
request_start_times = {}

latest_hand_results = {"Left": "None", "Right": "None"} # 좌/우 결과 저장
latest_hand_raw_labels = {} # 클래스 입력용 (점수 제외 순수 라벨)
latest_hand_landmarks_dict = {"Left": None, "Right": None} # 클래스 입력용 좌표

current_action_id = "ID_NONE"

# 손 랜드마크 그릴 떄 필요
# latest_hand_landmarks = None

# GestureRecognizer 인스턴스 생성
recognizer = GestureRecognizer()

"""
콜백 함수 정의 (AI 결과가 나오면 해당 함수 호출)
"""
def gesture_callback(result: vision.GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    global latest_hand_results, latest_hand_raw_labels, latest_hand_landmarks_dict

    # 레이턴시 계산 (AI 분석에 걸리는 시간)
    current_time = time.time() * 1000
    start_time = request_start_times.pop(timestamp_ms, None) # 시작 시간 가져오고 삭제
    latency = current_time - start_time if start_time else 0

    # 결과 초기화
    temp_labels = {}
    display_results = {"Left": "None", "Right": "None"}
    temp_landmarks = {"Left": None, "Right": None}
    #latest_hand_landmarks = result.hand_landmarks if result.hand_landmarks else None

    # 손 2개 인식 및 좌/우 구분 로직
    if result.gestures and result.handedness:
        # gestures와 handedness는 인덱스가 서로 대응됨
        for i in range(len(result.gestures)):
            gesture = result.gestures[i][0]
            gesture_label = gesture.category_name
            hand_label = result.handedness[i][0].category_name # "Left" 또는 "Right"
            
            display_results[hand_label] = f"{gesture_label} ({gesture.score:.2f})" # 제스처 정확도
            temp_labels[hand_label] = gesture_label # 클래스 전송용 모델 자체 출력 이름
            temp_landmarks[hand_label] = result.hand_landmarks[i] # 해당 손의 랜드마크 리스트 

    latest_hand_results = display_results
    latest_hand_raw_labels = temp_labels
    latest_hand_landmarks_dict = temp_landmarks

        # # 터미널 출력 (디버깅용)
        # print(f"[Latency] {latency:.1f}ms | L: {latest_hand_results['Left']} | R: {latest_hand_results['Right']}")


# 모터 제어용
def pose_callback(result: vision.PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    """포즈 인식 결과 처리 콜백"""
    pass


"""
모델 설정
"""
# hand recognize
base_options = mp.tasks.BaseOptions

hand_gesture_options = vision.GestureRecognizerOptions(
    base_options = base_options(
        model_asset_path = HAND_MODEL,
        delegate = python.BaseOptions.Delegate.GPU
    ),
    running_mode = vision.RunningMode.LIVE_STREAM,
    num_hands = 2,
    min_hand_detection_confidence = 0.7,
    result_callback = gesture_callback
)


# body
body_options = vision.PoseLandmarkerOptions(
    base_options = base_options(
        model_asset_path = POSE_MODEL,
        delegate = python.BaseOptions.Delegate.GPU
    ),
    running_mode = vision.RunningMode.LIVE_STREAM,
    result_callback = pose_callback
)

hand_gesture = vision.GestureRecognizer.create_from_options(hand_gesture_options)
body_landmarker = vision.PoseLandmarker.create_from_options(body_options)

cap = cv2.VideoCapture(0)
monitor = PerformanceMonitor()

if not cap.isOpened():
    raise RuntimeError('웹캠을 열 수 없습니다.')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 화면 설정
    h, w, _ = frame.shape
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)) # 색 변환, opencv로 불러오는거라 BGR로 불러오기 때문

    # 레이턴시 계산
    timestamp_ms = int(time.time() * 1000) # 타임스탬프 생성 (밀리초 단위)
    request_start_times[timestamp_ms] = timestamp_ms # 시작 시간 기록

    # 비동기 추론
    hand_gesture.recognize_async(mp_image, timestamp_ms)
    body_landmarker.detect_async(mp_image, timestamp_ms)

    # GesstureRecognizer 로직 실행
    # 콜백에서 업데이트된 최신 라벨과 랜드마크를 클래스에 전달
    current_action_id = recognizer.process_frame(latest_hand_raw_labels, latest_hand_landmarks_dict)

    # 화면 표시
    color = (0, 255, 0) if "CHOPSTICKS" in current_action_id or "DIAL" in current_action_id else (255, 255, 255)
    cv2.rectangle(frame, (w//2 - 200, 10), (w//2 + 200, 60), (0, 0, 0), -1) # 가독성 배경
    cv2.putText(frame, f"ACTION: {current_action_id}", (w//2 - 180, 45), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 3)

    # 왼손, 빨간색
    cv2.putText(frame, f"Left: {latest_hand_results['Left']}", (20, 150), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    # 오른손, 파란색
    cv2.putText(frame, f"Right: {latest_hand_results['Right']}", (20, 190), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # 손 랜드마크
    for side in ["Left", "Right"]:
        landmarks = latest_hand_landmarks_dict[side]
        if landmarks:
            for lm in landmarks:
                cv2.circle(frame, (int(lm.x * w), int(lm.y * h)), 3, (0, 255, 0), -1)
    
    stats = monitor.get_stats()
    monitor.draw_performance(frame, stats)
    
    cv2.imshow('Gesture Recognition Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 시 자원 해제 필수
hand_gesture.close()
body_landmarker.close()
cap.release()
cv2.destroyAllWindows()