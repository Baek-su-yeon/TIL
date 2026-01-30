import cv2
import mediapipe as mp
import os
import shutil
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# --- 설정 부분 ---
MODEL_PATH = 'models/hand_landmarker.task'  # 모델 파일 경로
INPUT_FOLDER = 'C:/Users/SSAFY/Desktop/data_collect/data/class_name'       # 이미지가 들어있는 폴더, 제일 뒤에 이름 폴더명으로 바꿀 것
OUTPUT_FOLDER = 'C:/Users/SSAFY/Desktop/data_collect/remove_data/class_name'      # 클릭 시 이동할 폴더

# 폴더 생성
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

class HandPicker:
    def __init__(self, model_path):
        # 1. Hand Landmarker 설정 (IMAGE 모드)
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.IMAGE,
            num_hands=2,
            min_hand_detection_confidence=0.5
        )
        self.detector = vision.HandLandmarker.create_from_options(options)
        self.move_requested = False

    def mouse_callback(self, event, x, y, flags, param):
        """마우스 왼쪽 클릭 시 이동 플래그 활성화"""
        if event == cv2.EVENT_LBUTTONDOWN:
            self.move_requested = True

    def draw_landmarks(self, frame, detection_result):
        """인식된 결과를 화면에 그리기"""
        if not detection_result.hand_landmarks:
            return frame

        annotated_image = frame.copy()
        h, w, _ = frame.shape

        for landmarks in detection_result.hand_landmarks:
            # 관절 그리기 (Tasks API 결과값은 x, y가 0~1 사이)
            for i, lm in enumerate(landmarks):
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(annotated_image, (cx, cy), 5, (0, 255, 0), -1)
                
            # 연결선 그리기 (필요 시 직접 구현하거나 mp.solutions.drawing_utils 사용 가능)
            # 여기서는 최신 API 유지와 가독성을 위해 점만 표시합니다.
        return annotated_image

    def run(self):
        # 지원하는 이미지 확장자
        extensions = ('.jpg', '.jpeg', '.png', '.bmp')
        files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(extensions)]

        cv2.namedWindow('MediaPipe Picker')
        cv2.setMouseCallback('MediaPipe Picker', self.mouse_callback)

        print(f"✅ 총 {len(files)}개의 이미지를 로드했습니다.")
        print("🖱️  [왼쪽 클릭]: 파일 이동 후 다음")
        print("⌨️  [아무 키]: 이동 없이 다음")
        print("⌨️  [ESC]: 종료")

        for file_name in files:
            file_path = os.path.join(INPUT_FOLDER, file_name)
            image = cv2.imread(file_path)
            if image is None: continue

            # MediaPipe용 이미지 객체 생성
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            
            # 추론 수행
            detection_result = self.detector.detect(mp_image)
            
            # 결과 시각화
            display_img = self.draw_landmarks(image, detection_result)
            
            # 화면 표시 및 대기
            self.move_requested = False
            while True:
                cv2.imshow('MediaPipe Picker', display_img)
                key = cv2.waitKey(1)

                if self.move_requested:
                    target_path = os.path.join(OUTPUT_FOLDER, file_name)
                    shutil.move(file_path, target_path)
                    print(f"📦 Moved: {file_name}")
                    break
                
                if key != -1: # 키보드 입력 시
                    if key == 27: # ESC
                        cv2.destroyAllWindows()
                        return
                    break # 다음 이미지로

        print("🏁 모든 처리가 끝났습니다.")
        cv2.destroyAllWindows()

if __name__ == "__main__":
    picker = HandPicker(MODEL_PATH)
    picker.run()