## 😎 프로젝트 소개
- 원티드 4주차 개인과제입니다. SNS API를 구현합니다. 게시판 CRUD, 필터링, 좋아요, 리스트 정렬 기능 등을 구현하였습니다.
- **1차 기능 개발, 2차 기능 개발**로 나누어서 구현하였습니다.
- **프로젝트 기간**: 2022년 7월 20일(수) ~ 2022년 7월 26일(화)

<br>

## 😃 기술 스택

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/djangorestframework-DC0032?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/SQLlite-003B57?style=for-the-badge&logo=SQLite&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

<br>

## 📕 이슈 내용

- **1차 개발**: 게시글 기본 CRUD
- **2차 개발**: 부가기능 추가
- **3차 개발**: 기능 고도화. 추가적인 기능 직접 정의하여 추가

<br>

## 📙 ERD

<p align="center">
 <img src = "https://user-images.githubusercontent.com/96091519/180701613-eb5f6458-587d-49a0-81eb-55381917b836.png", width="350px">
</p>


<br>

## 📒 API DOCUMENT

|Action| Method| URL|
|-----|----|----|
|회원가입| POST| users/signup
|로그인| POST| users/signin
|로그아웃| POST| users/signout
|게시물 작성| POST| posts
|게시물 리스트| GET| posts
|게시물 수정| PATCH| posts/<int:post_id>
|게시물 삭제, 취소| PATCH| posts/<int:post_id>/delete
|게시물 좋아요, 취소| GET| posts/<int:post_id>/likes

<br>

## 📗 1차 개발: 상세 내용

### 🌊 **01. 게시글 생성** ###
- [x] 완료 여부
- 필수 입력사항: 제목, 내용
- 작성자 정보는 request body가 아니라 토큰에서 추출함

***

### 🌊 **02. 게시글 수정** ###
- [x] 완료 여부
- 작성자만 수정 가능

***

### 🌊 **03. 게시글 삭제** ###
- [x] 완료 여부
- 작성자만 삭제 가능

***

### 🌊 **04. 게시글 상세보기** ###
- [x] 완료 여부
- 모든 사용자는 권한 상관없이 모든 사용자 열람 가능

***

### 🌊 **05. 게시글 목록** ###
- [x] 완료 여부
- 모든 사용자는 권한 상관없이 모든 사용자 열람 가능
- 제목, 작성자, 해시태그, 작성일, 좋아요 수, 조회수 포함됨

***

<br>
<br>


## 📘 2차 개발: 상세 내용

### 🤡 **01. 해시태그 입력** ###
- [x] 완료 여부
- 게시글 생성 시 필수 입력사항: 제목, 내용, **해시태그**
- 해시태그는 #으로 시작되고 , 로 구분되는 텍스트가 입력됨
- 예: {"hashtag": "#맛집, #서울, #브런치 카페, # 주말"}

***

### 🤡 **02. 게시글 삭제 후 복구** ###
- [x] 완료 여부
- 작성자만 삭제 가능
- delete_flag 이용해서 삭제, 복구 상태를 번갈아가며 리턴

***

### 🤡 **03. 좋아요 기능** ###
- [x] 완료 여부
- 작성자를 포함한 사용자는 게시글 상세보기에서 좋아요 누를 수 있음
- 좋아요 된 게시물에 다시 좋아요 누르면 취소됨

***

### 🤡 **04. 조회수 기능** ###
- [x] 완료 여부
- 작성자를 포함한 사용자가 게시글 상세보기 하면 조회수 1 증가함
- 횟수 제한은 없음. 무한히 증가 가능.

***

### 🤡 **05-(1). 게시글 목록 / Ordering (= Sorting, 정렬)** ###

- [x] 완료 여부
- 쿼리 파라미터로 구현함. 예: **?ordering=created_at**
- 사용자는 게시글 목록을 원하는 값으로 정렬 가능
- 오름차순, 내림차순 선택 가능

***

### 🤡 **05-(2). 게시글 목록 / Searching (= 검색)** ###
- [x] 완료 여부
- 쿼리 파라미터로 구현함. 예: **?searching=test**
- 사용자는 입력한 키워드로 해당 키워드를 포함한 게시물 조회 가능
- Like 검색, 해당 키워드가 문자열 중 포함된 데이터 검색함
- 검색 필드는 title이므로 제목에서만 검색됨.
- 검색 방법: some-url?search=후기 → '후기'가 제목에 포함된 게시글 목록
- 예: '후기' 검색 시 → 00 방문후기입니다. (검색됨)

***

### 🤡 **05-(3). 게시글 목록 / Filtering (= 필터링)** ###
- [ ] 완료 여부
- 쿼리 파라미터로 구현함. 예: **?hashtag=#test**
- 사용자는 지정한 키워드로 해당 키워드를 포함한 게시물 필터링 가능
- hashtag 필드만 지정했으므로 hashtag 기준으로 필터링 가능
- 검색방법: some-url?hashtag=서울 → '서울' 해시태그를 가진 게시글 목록
- 검색방법: some-url?hashtag=서울, 맛집 → '서울', '맛집' 해시태그 둘 다 포함 필요
- 예: '서울' 검색 시 → #서울(O) / #서울맛집(X) / #서울,#맛집(O)
- 예: '서울, 맛집' 검색 시 → #서울(X) / #서울맛집(X) / #서울,#맛집(O)

***

### 🤡 **05-(4). 게시글 목록 / Pagination (= 페이지 기능)** ###
- [x] 완료 여부
- 쿼리 파라미터로 구현함. 예: **?limit=10&offset=10**
- 사용자는 1페이지당 게시글 수를 조정할 수 있음 (limit)
- Default Limit: 10건

***

<br>
