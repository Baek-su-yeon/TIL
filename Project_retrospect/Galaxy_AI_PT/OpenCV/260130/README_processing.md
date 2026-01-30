# 🖐️ MediaPipe Hand Landmark Image Picker

이 프로젝트는 **MediaPipe Tasks API**를 사용하여 특정 폴더 내의 이미지에서 손 랜드마크를 검출하고, 시각화된 결과를 확인하며 사용자가 원하는 이미지만 별도의 폴더로 분류(이동)할 수 있게 돕는 툴입니다.

## 📌 주요 기능

* **실시간 랜드마크 시각화**: 이미지 내의 손가락 마디 및 관절을 화면에 표시합니다.
* **간편한 데이터 분류**: 마우스 왼쪽 클릭 한 번으로 이미지를 지정된 폴더로 이동시킵니다.
* **넘기기 기능**: 이동을 원치 않는 이미지는 키보드 아무 키나 눌러 빠르게 다음으로 넘어갈 수 있습니다.

## 🛠️ 사전 준비

터미널(또는 Anaconda Prompt)을 열고 아래 명령어를 순서대로 입력하여 개발 환경을 구축합니다.

### **가상환경 생성**

```bash
# 가상환경 이름은 마음대로 생성 (Python 3.11 권장)
conda create -n YOUR_ENV_NAME python=3.11 -y

```

### **가상환경 활성화**

```bash
conda activate YOUR_ENV_NAME

```

### **필수 라이브러리 설치**

```bash
# 프로젝트 루트 디렉토리에서 실행
pip install -r requirements.txt

```

## 🚀 사용 방법

### 1. 경로 설정

코드 상단의 설정 변수를 본인의 환경에 맞게 수정합니다.

```python
MODEL_PATH = 'models/hand_landmarker.task'  # 모델 파일 경로 (변경 필요 ❌)
INPUT_FOLDER = 'data/class_name'       # 이미지가 들어있는 폴더, class_name은 확인 후 변경 필요
OUTPUT_FOLDER = 'remove_data/class_name'      # 클릭 시 이동할 폴더, class_name은 확인 후 변경 필요

```

### 2. 실행

```bash
# 제일 상단 폴더에서
python -m image_processing.py

```

### 3. 조작 가이드

| 동작 | 결과 |
| --- | --- |
| **마우스 왼쪽 클릭** | 현재 이미지를 `OUTPUT_FOLDER`로 **이동**하고 다음 이미지 표시 |
| **아무 키 입력** | 이동하지 않고 다음 이미지로 넘어감 (Skip) |
| **ESC 키** | 프로그램 종료 |


## ⚠️ 주의 사항

* 이 코드는 `shutil.move`를 사용합니다. 즉, 클릭 시 원본 폴더에서 파일이 **삭제되고 이동**됩니다.
* 이미지에 손이 감지되지 않더라도 화면은 표시되며, 클릭 시 동일하게 이동됩니다. (손이 감지되지 않으면 랜드마크도 안그려질 것임 이동시키기)
