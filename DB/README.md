# 📅 학습 현황 (목차)

현재까지 다음과 같은 주제에 대한 정리가 완료되었습니다.

| 번호 | 주제 | Markdown (.md) | Reference / Sub-notes (.md) |
| --- | --- | --- | --- |
| **1** | **Relational Database & SQL Basic** | [1. SQL_251210.md](https://www.google.com/search?q=1.%2520SQL_251210.md) (2025.12.10) | - |
| **2** | **DDL, DML & JOIN** | [2. SQL_251211.md](https://www.google.com/search?q=2.%2520SQL_251211.md) (2025.12.11) | - |
| **3** | **Many-to-One Relationships** | [3.Many_to_One_Relationships_251217.md](https://www.google.com/search?q=3.Many_to_One_Relationships_251217.md) (2025.12.17) | - |

---

## 📚 주제별 상세 내용

### 1. Relational Database & SQL Basic

* **Relational Database (RDB)**: 테이블, 행, 열로 구조화된 데이터 모음과 관련 키워드 정리
* **SQL Statements Types**: DDL(구조 정의), DQL(검색), DML(조작), DCL(권한 제어)의 이해
* **SELECT (DQL)**:
* `FROM` ➡ `WHERE` ➡ `GROUP BY` ➡ `HAVING` ➡ `SELECT` ➡ `ORDER BY` ➡ `LIMIT` 순의 실행 순서 파악
* 다양한 필터링 조건(`LIKE`, `BETWEEN`, `IN`) 및 집계 함수 활용



### 2. DDL, DML & JOIN

* **DDL (Data Definition Language)**: `CREATE`(생성), `ALTER`(수정 - 필드 추가/이름 변경/삭제), `DROP`(테이블 삭제)
* **DML (Data Manipulation Language)**: `INSERT`(삽입), `UPDATE`(수정), `DELETE`(삭제) 및 조건절 활용
* **JOIN**:
* **INNER JOIN**: 교집합 데이터 조회
* **LEFT JOIN**: 왼쪽 테이블 기준 전체 데이터 및 매칭되지 않는 데이터의 NULL 처리



### 3. Many-to-One Relationships (N:1 관계)

* **모델 관계 종류**: 1:1, N:1(여러 레코드가 하나에 연결), N:M 관계의 특징 및 예시
* **Foreign Key (외래 키)**:
* N:1 관계에서 N측 테이블에 위치하며 부모의 PK를 저장
* `on_delete` 속성(CASCADE, PROTECT, SET_NULL)을 통한 참조 무결성 관리


* **모델 참조 및 역참조**:
* **참조**: 자식 객체에서 부모 객체를 조회
* **역참조**: 부모 객체에서 자신을 참조하는 자식 객체들을 조회하는 `related_manager`(`model_set`) 활용법