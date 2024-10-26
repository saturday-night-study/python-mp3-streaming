# mp3 web player
테스트를 위해 임시 서버 https://xym0.kalee.land:10443/docs 에서 확인 가능하도록 하였습니다.

## 모듈 구성
### mp3.reader
### mp3.trimmer
### mp3.streamer 

## 실행 방법 
해당 프로젝트는 `poetry`를 기반으로 만들어졌습니다. 반드시 실행 전 `poetry` 설치가 필요합니다.

### poetry 명령어
```sh
poetry install  # 환경 기본 설치
poetry shell    # 가상 shell 진입
poetry build    # 패키지 빌드
```

### 서버 실행 명령어
```sh
uvicorn main:app --reload --host 0.0.0.0 --port 10001 # 외부 오픈을 위해서는 host가 0.0.0.0으로 되어야함
```

