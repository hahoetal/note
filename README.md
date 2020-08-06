# note


## 홈
- 앱 -> main

## 계정 관리
- account 앱
- 장고 자체 User 모델 사용
- 로그인 -> LoinView 사용
- 로그아웃 -> LogoutView 사용

## 쪽지
- message 앱
- Note 모델 생성<br>
보내는 사람(sender)만 foreignkey를 이용해 User 모델과 연결하고 받는 사람(receiver)은 CharField로 설정.<br>
둘 다 외래키로 설정하는 건 안 되는 것 같고 방법을 모르겠음...
- 기능은 '쪽지 보내기', '보낸 쪽지만 보기', '받은 쪽지만 보기'

### 추가하거나 보충할 것.
- 쪽지 읽음 표시하기
- 꾸미기
- 동시에 여러명에게 쪽지를 보낼 수 있게 만들기
