본 폴더는 Django 프레임워크 학습 과정을 정리한 기록입니다.
파일 이름은 `[번호].[주제]_[날짜].확장자` 형식으로 구성되며, 번호는 주제 순서를 의미합니다.

> **⚠️ Notice**
>
> 본 학습 내용을 바탕으로 작성된 실습 코드 및 프로젝트 파일은 저작권 문제로 인해 **Private Repository**에서 별도로 관리되고 있습니다.

---

## 📅 학습 현황 (목차)

현재까지 다음과 같은 주제에 대한 정리가 완료되었습니다.

| 번호 | 주제 | Markdown (.md) | Reference / Sub-notes (.md) |
| :---: | :--- | :--- | :--- |
| **1** | **Django Basic & Template** | [1. basic&Template_251208.md](1.%20basic&Template_251208.md) (2025.12.08) | [0. Built_in_Filters_Template_Tags.md](0.%20Built_in_Filters_Template_Tags.md) |
| **2** | **Model & Database** | [2. Model_251208.md](2.%20Model_251208.md) (2025.12.08) | [0. Field_types_&_Field_options.md](0.%20Field_types_&_Field_options.md) |
| **3** | **ORM (Object-Relational Mapping)** | [3. ORM_251209.md](3.%20ORM_251209.md) (2025.12.09) | - |
| **4** | **Django Form** | [4. Form_251210.md](4.%20Form_251210.md) (2025.12.10) | [0. Built_in_Widgets_251210.md](0.%20Built_in_Widgets_251210.md) |

---

## 📚 주제별 상세 내용

### 1. Django Basic & Template
* **Django Design Pattern**: MVC 패턴과 유사하지만 명칭이 다른 **MTV (Model, Template, View)** 패턴의 개념 및 역할 정리
* **Project & App Structure**: `settings.py`, `urls.py` 등 프로젝트 구조와 `models.py`, `views.py` 등 앱 구조의 역할 이해
* **Template Language (DTL)**:
    * **Variable**: `{{ variable }}` 형태의 데이터 출력 및 `.`(dot) 접근법
    * **Filters**: `date`, `length`, `truncatechars` 등 약 60개의 Built-in 필터 활용
    * **Tags**: `for`, `if`, `block`, `extends` 등 제어 흐름을 위한 태그 정리
* **HTML Form**: `action`, `method`, `name` 속성의 역할 및 `input` 태그의 `type` vs `value` 차이점
* **Troubleshooting**: `AttributeError: 'tuple' object has no attribute 'get'` (View 반환값 튜플 오타 주의)

### 2. Model & Database
* **Model Definition**: DB 테이블을 Python 클래스로 정의하는 방법 및 스키마 설계 (Todo, Book 모델 예시)
* **Field Types & Options**:
    * `CharField`(`max_length` 필수), `TextField`, `IntegerField` 등 주요 필드 타입 정리
    * `null` (DB), `blank` (유효성 검사), `primary_key` 등 주요 옵션 정리
* **Migrations**: `makemigrations` (설계도 생성) 및 `migrate` (DB 반영) 과정의 이해
* **Admin Site**: `createsuperuser`를 통한 관리자 생성 및 모델 등록(`admin.site.register`)
* **Troubleshooting**: `IntegrityError: NOT NULL constraint failed` (필수 필드 누락 시 발생)

### 3. ORM (Object-Relational Mapping)
* **QuerySet API**: 객체와 DB 데이터를 매핑하는 기술
    * **조회 메서드**: `all()` (전체), `filter()` (조건 포함, QuerySet 반환), `get()` (단일 객체 반환)
* **Field Lookups**: `필드명__조건` 형태의 상세 조회 기술
    * `exact`, `iexact`, `contains` (포함 여부), `gt`/`lt` (대소 비교), `startswith` 등 주요 Lookup 정리

### 4. Django Form
* **Form Class**: 사용자 입력 데이터 수집, 유효성 검사 자동화, 오류 처리 등을 수행하는 도구
* **ModelForm**: Model 클래스와 결합하여 DB 필드를 기반으로 폼을 자동 생성하는 기능
    * **Meta Class**: 폼 동작 제어를 위해 연결할 모델(`model`)과 사용할 필드(`fields`) 정의
    * **save()**: 데이터베이스 객체를 생성 및 저장 (instance 인자를 통해 수정 모드 지원)
* **Widgets**: `TextInput`, `PasswordInput` 등 HTML 렌더링 방식을 제어하는 옵션
* **Form vs ModelForm**:
    * **Form**: DB 저장이 필요 없는 경우 (예: 로그인, 검색)
    * **ModelForm**: DB 저장이 필요한 경우 (예: 회원가입, 게시글 작성)