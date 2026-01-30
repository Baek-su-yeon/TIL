from src.utils.utils import Datacollector
import cv2
import time

def on_mouse_click(event, x, y, flags, param):
    # 1. 왼쪽 버튼 클릭: 단일 사진 촬영
    if event == cv2.EVENT_LBUTTONDOWN:
        param.save_flag = True
    
    # 2. 오른쪽 버튼 누름: 연속 촬영 시작
    elif event == cv2.EVENT_RBUTTONDOWN:
        param.continuous_flag = True
        print("연속 촬영 시작...")

    # 3. 오른쪽 버튼 뗌: 연속 촬영 중지
    elif event == cv2.EVENT_RBUTTONUP:
        param.continuous_flag = False
        print("연속 촬영 중지")

collector = Datacollector(model_path='models/hand_landmarker.task')
collector.set_gesture("Call_Hand") # 수집할 데이터 클래스명으로 수정
collector.save_flag = False
collector.continuous_flag = False  # 연속 촬영용 플래그 초기화

cap = cv2.VideoCapture(0)
cv2.namedWindow('Collection_Window')
cv2.setMouseCallback('Collection_Window', on_mouse_click, collector)

# 초기 성능 모니터링용 (선택사항)
start_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    # [중요] 타임스탬프 생성 (밀리초 단위)
    timestamp_ms = int((time.time() - start_time) * 1000)

    # 1. 비동기로 추론 요청 (화면이 끊기지 않음)
    collector.detect_async(frame, timestamp_ms)

    # 단일 촬영(L) 혹은 연속 촬영(R) 중일 때 저장
    if collector.save_flag or collector.continuous_flag:
        collector.save_frame(frame)
        # 단일 촬영 플래그는 저장 후 즉시 초기화
        if collector.save_flag:
            collector.save_flag = False

    # 3. 화면 표시용 가공
    debug_frame = frame.copy()
    # collector.latest_landmarks에 담긴 가장 최신 정보를 가져와서 그림
    collector.draw_landmarks_manual(debug_frame, collector.latest_landmarks)
    
    # 가독성을 위해 거울 모드 적용 권장
    display_frame = cv2.flip(debug_frame, 1)

    # 현재 상태 표시 (연속 촬영 중이면 빨간색 텍스트 표시)
    status_text = "RECORDING" if collector.continuous_flag else "LIVE_STREAM"
    status_color = (0, 0, 255) if collector.continuous_flag else (255, 255, 0)
    
    cv2.putText(display_frame, f"Count: {collector.count}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(display_frame, "LIVE_STREAM MODE", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
    
    cv2.imshow('Collection_Window', display_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()