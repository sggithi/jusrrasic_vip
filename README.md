# ExploreCSR


과제로 수행한 walking detection 모델을 활용한 게임 제작
 

## 기본 구성
뼈대코드는 https://codesandbox.io/s/sleepy-blackburn-ixxn0?file=/src/readme.md:606-625 를 참고한다. 


## 기본스펙

뼈대 코드를 기본으로 하여 다음이 구현되어 있어야 한다.  
모든 행동들은 서버에서 이루어지나, 클라이언트에서 별도로 확인이 가능하여야 한다.(html 결과창에 결과가 프린트되면된다)
- 온라인에서 플레이가 가능하다( codesandbox 등을 활용)  
- 로그인, 회원가입  
- 10 * 10 이상의 맵  
- 캐릭터의 이동  
- 이동 시 필드별로 아무일도 일어나지 않음, 전투, 아이템 획득의 일이 일어남.
- 5종 이상의 몬스터  
- 5종 이상의 아이템  
- 전투 시스템( str, def, hp 개념을 활용)  
- 사망 시스템(전투 시 hp가 0이될 경우 캐릭터, 가 사망. 0,0 위치로 이동)  
- 레벨 시스템( 일정 이상 경험치 획득 시 캐릭터 레벨업.)

## 추가스펙

추가 스펙은 조별로 구현가능한 부분을 구현하면 된다.


- 체력회복하는 이벤트가 추가된다.
- 필드에서 일어나는 이벤트 중 랜덤이벤트가 존재한다.  
- 아이템을 소유할 경우, 캐릭터의 능력치가 향상된다. 능력치가 클라이언트에서 확인이 가능하다.  
- 시작 능력치가 랜덤하게 주어지며, 5번에 한하여 재시도가 가능하다. 
- 사망시 랜덤하게 아이템을 잃어버린다.  
- 유저의 인벤토리가 클라이언트 상에서 확인이 가능하다. 
- 전투 중, 10턴 안에 전투가 끝나지 않거나, 체력이 20% 이하로 감소할 경우 도망가는 선택지가 추가로 주어진다.

