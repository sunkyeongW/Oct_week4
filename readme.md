# Python
    프로그래밍 언어 종류 중 하나.
    인터프리터 언어(코드를 바로 실행할 수 있는 언어)에 속함.

# 실행 
    1. shell로 실행 :
        interactive mode(상호 작용)
            ;(세미콜론) 사용 시 여러 명령을 한번에 실행.
            ;\ 사용 시 명령을 유보 시킨 후 실행.

    2. file로 실행 :
        반복, 복잡한 코드 작성 시 유용함.

# 데이터 타입
    1. 숫자형 데이터 타입(Number Type)
        -Int(정수형)
        -Float(실수형)
    2. 문자형 데이터 타입(Text Type)
        -string(문자)
    3. 리스트 데이터 타입(List Type)
        - 다양한 종류, 갯수의 데이터들을 정리할 때 유용하게 쓰임.
        - 통계에서 유용.

# 변수
    하나의 값을 저장할 수 잌ㅆ는 저장공간.

# 입력과 출력
    -input : file, keyboard
    -output : sound, monitor

# pypi
    파이썬으로 만든 패키지들을 관리하고 열람할 수 있는 저장소.

# DB의 목적
    SQL(DB서버에 요청하기 위한 언어)이라는 컴퓨터 언어를 통해서 데이터 제어 가능.
    DB의 데이터들을 앱이나 웹을 이용해 다른 유저에게도 공유 가능.

# MySQL 접속
    mysql -uroot -p : mysql 접속

# MySQL 구조
    표 < 데이터베이스(스키마) < 데이터베이스 서버
    표(table) : 데이터를 기록하는 공간
        -수평구조(row, 행)
        -수직구조(column, 열)
    데이터베이스 : 표를 그루핑한 곳
        -데이터베이스(스키마)가 모여 데이터 베이스 서버 안에 저장.

# MySQL 스키마(schema)
    CREATE DATABASE DB이름 : DB 생성.
    DROP DATABASE DB이름 : DB 삭제.
    USE DB이름 : DB 선택.

# MySQL의 표(table) 생성
    CREATE TABLE [table이름] () : 테이블 생성.
        -INT : 정수만 등록 가능
        -NOT NULL : 빈칸 불가
        -AUTO_INCREMENT : 값 자동 증가
        -VARCHAR : 최대 글자 개수

# MySQL의 CRUD
    Create : INSERT INTO [테이블이름] () VALUES ()
    Read : 
        -생성된 데이터 출력 : SELECT * FROM [테이블 이름]
        -특정 값만 출력 : WHERE [TABLE 행]='특정 값'
        -정렬 : ORDER BY 원하는 정렬방식
        -데이터 수 지정 : LIMIT
    Update : UPDATE SET 행='수정값' WHERE ID값
    Delete : DELETE FROM [테이블] WHERE ID값

# 관계형 데이터베이스의 필요성
    장점: 별도의 데이터 테이블을 중복을 방지하여 유지 보수가 쉬움.
    단점: 별도의 표를 열어 비교해봐야 하기 때문에 직관적이지 않음.

# MySQL JOIN
    분리된 테이블을 읽을 때 통합해서 보여주기가 가능.
    SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.id;
    
    AS : 행을 바꾸고 싶을때 사용.

# DATABASE SERVER
인터넷 위에서 동작하는 컴퓨터들은 정보를 요청과 응답으로 주고 받음.
    요청하는 곳 : client(클라이언트)
    응답하는 곳 : server(서버)


    데이터베이스 클라이언트 <-> 데이터베이스 서버
        데이터베이스 클라이언트는 MySQL이라는 명령어 기반의 프로그램을 이용.

# MySQL Client
    MySQL monitor : 명령어 기반, 어디서든 사용할 수 있는 프로그램.
    MySQL workbench : GUI 기반

# MySQL workbench
    


    