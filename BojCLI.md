# Baekjoon Online Judge용 커맨드라인 인터페이스

```shell
$ ./index 1000
Your answer is good for in/output samples
```

## 사용법

루트 폴더에서 다음 명령 실행시 [Baekjoon Online Judge]의 문제를 가져오거나 채점합니다. (problem_number는 문제 번호 숫자)

```shell
./index [problem_number]
```

문제에 대한 첫 실행 시, 프로그램은 해당 문제의 첫 번째 예제 입력과 출력을 가져와 `[problem_number].input.txt`와 `[problem_number].output.txt`으로 저장하고 해당 문제 페이지를 구글 크롬으로 띄우며 문제 링크를 최상단에 위치시킨 빈 파이썬 파일을 생성하고 이를 VS코드로 엽니다.

이후 실행시에는 `[problem_number].py`에 `[problem_number].input.txt`을 입력으로 사용하여 출력을 `[problem_number].your.txt`에 저장하고 이를 예제 출력과 비교합니다.

### 주의사항

- 이 프로그램은 매우 [@lens0021]를 위하여 작성되어 있어 다른 용도의 사용에는 불편함이 있습니다. 포크하여 수정하기도 불편할 것으로 예상되는 바, 필요한 경우에는 코드를 참고하여 새 프로그램을 만드는 것을 권하여 드립니다.
- 예제 입력이 둘 이상인 경우 불러와지지 않으니 직접 추가하여야 합니다.

## 의존성

- Node(for fetching in/output samples)
- Visual Studio Code(as just a text editor)
- git(for diff engine)
- Google Chrome

## 설치 방법

```shell
npm install
```

[baekjoon online judge]: https://www.acmicpc.net/
[@lens0021]: https://github.com/lens0021
