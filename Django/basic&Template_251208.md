## Django Design pattern
-소프트웨어 설계에서 반복적으로 발생하는 문제에 대한 검증되고 재사용 가능한 일반적인 해결책
✳ Django는 기존 MVC 패턴과 동일하나 명칭을 달리 정의한 MTV 패턴을 가짐

|MVC|MTV|설명|
|:---|:---|:---|
|Model|Model|데이터 및 비즈니스 로직 처리|
|View|Template|사용자에게 보이는 화면 담당|
|Controller|View|사용자의 입력을 받아 Model과 View를 제어|

---

## 프로젝트 및 앱 구조
### 프로젝트 구조

| 이름 | 설명 |
| :--- | :--- |
| **settings.py** | 프로젝트의 모든 설정 관리 |
| **urls.py** | 요청 들어오는 URL에 따라 이에 해당하는 적절한 Views 연결 |
| **\_\_init\_\_.py** | 해당 폴더를 패키지로 인식하도록 설정하는 파일 |
| **asgi.py** | 비동기식 웹 서버와의 연결 관련 설정 |
| **wsgi.py** | 웹 서버와의 연결 관련 설정 |
| **manage.py** | Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티 |

### 앱 구조

| 이름 | 설명 |
| :--- | :--- |
| **admin.py** | 관리자용 페이지 설정 |
| **models.py** | DB와 관련된 Model을 정의, MTV 패턴의 M |
| **views.py** | HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환<br>url, model, template과 연동, MTV 패턴의 V |
| **apps.py** | 앱의 정보가 작성된 곳 |
| **tests.py** | 프로젝트 테스트 코드를 작성하는 곳 |

---

## Template Language
- **Template System**: 파이썬 데이터를 HTML 문서와 결합에 로직과 표현을 분리한 채 동적인 웹페이지를 생성하는 도구 (**페이지 틀**에 **데이터**를 동적으로 결합)
- **Template Language**: Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

    ### 1. Variable
    - render 함수의 세번째 인자로 **딕셔너리 타입**으로 전달
    - 해당 딕셔러니 key에 해당하는 문자열이 template에서 사용 가능한 변수명
    - dot('.')을 사용하여 변수 속성에 접근
    ```django
    # views.py
    context = {
        'variable_1':'value_1',
        'variable_2':{
            'attribute':'value_2',
        },
    }
    # template.html
    {{ variable_1 }}
    {{ variable_2.attribute }}
    ```
    ### 2. Filters
    - 표시할 변수를 수정할 때 사용 (변수 + | + 필터)
    - chained(연결)이 가능하며 일부 필터는 인자를 받기도함
    - 약 60개의 built-in template filters를 제공
    ```django
    {{ variable_name|filter_name }} {# 기본 문법 #}
    {{ name|truncatewords:30 }}
    {# 예시, name 변수에 담긴 텍스트를 단어 30개까지만 보여줌 #}
    {# 30개를 넘어가면 말줄임표로 표시, 주로 게시글 미리보기 등에 사용 #}
    ```
    ### 3. Tages
    - 반복 또는 논리를 수행하여 제어 흐름 생성
    - 일부 태그는 시작과 종료 태그 필요
    - 약 24개의 built-in template tages 제공
    ```django
    {# if, else, endif #}

    {# views.py #}
    context = {
        'login': False,
    }

    {# template.html #}
    {% if login %}
        <h1>Hello, User!!</h1> {# login == True #}
    {% else %}
        <h1>Please, login</h1> {# login == False #}
    {% endif %}
    ```
    ```django
    {# for #}

    {# views.py #}
    context = {
        'nums': [1,2,3],
    }

    {# template.html #}
    <ul>
        {% for num in nums %}
            <li>{{ num }}</li>
        {% endfor %}
    </ul>
    {% comment %}
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
    </ul>
    {% endcomment %}
    ```

---

## HTML form
- **'form' element**: 사용자로부터 할당된 데이터를 서버로 전송하는 HTML 요소
    ### 속성
    |속성명|설명|
    |:---|:---|
    |action|입력 데이터가 전송될 URL(✳ 기본값 = 현제 페이지의 URL)|
    |method|데이터 전송 방식 정의 (GET, POST 등)|
    |input|사용자의 데이터를 입력 받는 요소(✳ type 속성 값에 따라 입력 데이터 유형 상이)|
    |name|사용자가 입력한 데이터의 이름(= key), 서버에서 접근 시 해당 속성값 이용|
    ```HTML
    {% extends 'app_name/base.html' %}

    {% block content %}
        <form action = "URL" method = "POST">
            <label for="message">검색어</label>
            <input type="text" name="query" id="message">
            <input type="submit" value="submit">
        </form>
        <!-- URL에 데이터 입력 후 URL 결과-->
        <!-- https://URL?query=hello -->
        <!-- input의 name 속성에 입력한 데이터 할당 -->
    {% endblock %}
    ```
    ### request 객체
    - Django로 들어오는 모든 요청 관련 데이터 관리(✳ view 함수가 호출될 때 첫번째 인자로 전달)
    ```python
    # views.py
    def catch(request):
        print(request)
        print(type(request))
        print(dir(request))
        print(request.GET)
        print(request.GET.get('message'))
        return render(request, 'template/catch.html')
    
    """
    출력 결과
    <WSGIRequest: GET '/catch/?message=~~~'>
    <class 'django.core.handlers.wsgi.WSGIRequest'>
    ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', ...생략...]
    <QueryDict: {'message':['안녕!']}>
    안녕!
    """
    ```

---

## 참고
### input 속성: type vs value
| 속성 | 역할 (무엇을 정의하는가?) | 비유 | 작성하신 코드 예시 |
| :--- | :--- | :--- | :--- |
| **type** | **입력 요소의 종류(모양)**<br>텍스트 상자, 비밀번호 창, 버튼 등 형태를 결정 | 그릇의 종류<br>(밥그릇, 물컵, 접시) | `type="text"`<br>→ 글자 입력칸 생성<br>`type="submit"`<br>→ 제출 버튼 생성 |
| **value** | **입력 요소의 값(내용)**<br>입력창의 초기값이나 버튼 위에 적힐 글자 | 그릇 내용물<br>(쌀밥, 물, 반찬) | `value="submit"`<br>→ 버튼 위에 "submit" 글자 표시 |