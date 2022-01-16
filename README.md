# backjoon
1. 동적 프로그래밍 (Dynamic Programming, DP)

  사용 조건
   1. 최적 부분 구조 : 큰 문제를 작은 문제로 나눌 수 있다
   2. '중복'되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결한다. (ex. 점화식 존재)
  분할정복 기법 : 큰 문제를 작은 여러개의 문제로 나누어서 푸는 기법 (ex. 퀵 정렬)
  
  메모이제이션(Top-down) : 동적 프로그래밍 구현 방법
                        : 이전에 계산했던 값을 저장해두었다가 나중에 재사용하는 방법
                        : 반복적으로 계산되는 것의 계산 횟수를 줄일 수 있음
  상향식 계산법(Bottom-up)
  대표 문제
    1. 막대기 자르기
    2. 최장 공통 부분 수열 문제
    3. 0/1 배낭 문제
    
2. 그리디 알고리즘(Greddy Algorithm)
  선택의 순간마다 당장 눈앞에 보이는 최적의 상황만을 쫓아 최종적인 답에 도달하는 방법
  
  순서
  1. 선택 : 현재 상태에서 최적의 답 선택
  2. 적절성 검사 : 선택한 해가 문제의 조건을 만족하는지 검사
  3. 해답 검사: 원래의 문제가 해결되었는지 검사, 해결x면 선택절차로 돌아감.

  조건
  1. 탐욕적 선택 속성 : 앞의 선택이 이후의 선택에 영향x
  2. 최적 부분 구조 : 문제에 대한 최종 해결 방법은 부분 문제에 대한 최적 문제 해결 방법으로 구성됌.
