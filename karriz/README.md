# Python MP3 Streaming Server

## Goal
해당 프로젝트의 목표는 `TDD(Test-Driven Development)`를 익히는데 있으며, AI 스터디 이전에 Python 언어에 익숙해지는 것이다.

그리고 최종적으로는 근육에 각인이 될 수 있도록 머리가 생각하기 이전에 테스트 코드를 먼저 작성하는 습관을 들이는 것도 함께한다. 🤣

## TDD(Test-Driven Development)
TDD는 말그대로 테스트 주도형 개발로, 개발 방법론 중 하나이다. TDD는 `클린 코드(Clean Code)`를 기반으로 하여 코드의 복잡도를 낮춰 `단위 기능(Unit Functions)`의 오류율을 낮추기 위해 등장했다. 오류율을 낮추기 위해서 항상 `실패 상황(Fail-Case)`을 먼저 정의하고 해당 실패 상황들을 `성공 상황(Success-Case)`으로 변경하기 위해 최소 단위의 함수를 개발하고 이후 `코드 리팩토링(Code Refactoring)`과정을 통해 지저분하지 않고 깔끔한 코드가 되도록 해야한다.

### RGR(Red-Green-Refactor) Pattern
앞서 말했던 실패 -> 성공 -> 코드 리팩토링 과정을 하기 위한 방법이다.
  + `Red` : **실패**하는 테스트 코드 작성
  + `Green` : 실패 테스트 코드가 **성공**하도록 작성
  + `Refactor` : 통과 된 테스트 코드를 **리팩터링**하기

### Unit Test
`단위 테스트(Unit Test)`는 TDD의 **Clean code that works**를 지키기 위해서 반드시 함께 작성 되어야하는 테스트 코드이다.

단위 테스트와 TDD를 착각하는 경우가 많은데, 두 방식은 아래와 같은 차이가 있다.
  + **TDD**: 설계 프로세스
  + **단위 테스트**: 정밀한 테스트 케이스

### FIRST
단위 테스트를 작성할때는 *Robert C. Matin*이 제안한 `FIRST` 규칙을 따라 작성 되면 좋다.
  + `Fast` : 단위 테스트의 테스트 속도는 ms단위로 동작해야함
  + `Independent` : Unit을 벗어나는 데이터가 종속되면 안됨
  + `Repeatable` : 어떠한 환경에서 반복이 가능해야함
  + `Self-Validating` : 단위 테스트에 대한 검증은 스스로 해야함
  + `Timely` : 단위 테스트는 실제 코드 구성 이전에 작성 되어야함

## Study Plan (1~4 Week)

### 1 Week
1. MP3 파일 불러오기
  + constructor(filePath:string)  
    특정 경로의 MP3 파일을 읽어온다

  + parse() -> MP3File
    특정 경로의 MP3 파일을 읽고 MP3File 객체를 전달함
2. MP3 파일의 프레임의 구조 출력

### 2 Week
3. 전체 프레임 수 조회
  + frame_length() -> int
    파싱이 완료 된 MP3File의 총 프레임 수를 조회한다

4. MP3 전체 재생 시간 계산
  + get_play_time() -> int
    MP3 파일의 재생 시간을 계산한다

5. 특정 시간 영역 잘라 MP3File을 전달
  + constructor(mp3file: MP3File)
    트리밍 할 MP3파일을 지정한다.

  + trim() -> MP3File
    특정 MP3File을 기록 한다. 

### 3 Week
6. TCP Socket을 사용한 웹서버 구현 
7. URL 핸들러

### 4 Week
8. MP3 스트리밍
9. 오디오 배속 조절 기능
