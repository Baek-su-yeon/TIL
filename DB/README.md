본 폴더는 Database 및 SQL 학습 과정을 정리한 기록입니다.
파일 이름은 `[번호].[주제]_[날짜].확장자` 형식으로 구성되며, 번호는 주제 순서를 의미합니다.

> **⚠️ Notice**
>
> 본 학습 내용을 바탕으로 작성된 실습 코드 및 프로젝트 파일은 저작권 문제로 인해 **Private Repository**에서 별도로 관리되고 있습니다.

---

## 📅 학습 현황 (목차)

현재까지 다음과 같은 주제에 대한 정리가 완료되었습니다.

| 번호 | 주제 | Markdown (.md) | Reference / Sub-notes (.md) |
| :---: | :--- | :--- | :--- |
| **1** | **Relational Database & SQL Basic** | [1. SQL_251210.md](1.%20SQL_251210.md) (2025.12.10) | - |
| **2** | **DDL, DML & JOIN** | [2. SQL_251211.md](2.%20SQL_251211.md) (2025.12.11) | - |

---

## 📚 주제별 상세 내용

### 1. Relational Database & SQL Basic
* **Relational Database (RDB)**: 테이블, 행, 열로 구조화된 데이터 모음과 관련 키워드 정리
* **SQL Statements Types**:
    * **DDL**: 구조 정의 (CREATE, DROP, ALTER)
    * **DQL**: 데이터 검색 (SELECT)
    * **DML**: 데이터 조작 (INSERT, UPDATE, DELETE)
    * **DCL**: 권한 제어 (COMMIT, ROLLBACK 등)
* **SELECT (DQL)**:
    * **Basic**: `SELECT`, `FROM`, `AS`(Alias) 활용 및 산술 연산
    * **Execution Order**: `FROM` ➡ `WHERE` ➡ `GROUP BY` ➡ `HAVING` ➡ `SELECT` ➡ `ORDER BY` ➡ `LIMIT` 순서의 이해
    * **Filtering**: `WHERE` 절을 이용한 조건 조회 (`LIKE`, `IN`, `BETWEEN`, `IS NULL`)
    * **Grouping & Sorting**: `GROUP BY`와 `HAVING`을 통한 집계, `ORDER BY`를 통한 정렬, `LIMIT`을 통한 개수 제한

### 2. DDL, DML & JOIN
* **DDL (Data Definition Language)**:
    * **CREATE**: 테이블 생성 및 데이터 타입(`TEXT`, `INTEGER` 등), 제약 조건(`NOT NULL`, `PK`, `FK`) 정의
    * **ALTER**: `ADD COLUMN`, `RENAME`, `DROP COLUMN` 등을 이용한 테이블 구조 변경
    * **DROP**: 테이블 삭제
* **DML (Data Manipulation Language)**:
    * **INSERT**: 데이터 삽입 (단일 및 다중 레코드)
    * **UPDATE**: 데이터 수정 (WHERE 조건 활용)
    * **DELETE**: 데이터 삭제 (서브쿼리 활용 가능)
* **JOIN**:
    * **INNER JOIN**: 두 테이블 간 교집합(일치하는 값) 조회
    * **LEFT JOIN**: 왼쪽 테이블 기준 전체 조회 및 매칭되지 않는 오른쪽 데이터는 NULL 처리