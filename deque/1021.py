# 문제를 이해하는데 시간이 좀 걸렸다
# 예제 입력 2를 시행하면 내 생각엔 5가 출력인데, 왜 8인지.. --> 이 문제에서는 뒤에서는 뺄 수 없다! 앞에서만 원소를 뺄 수 있다
# queue : FIFO
# deque : 양방향에서 삽입, 삭제 가능

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # queue의 크기 N, 뽑아내려는 수의 개수 M
position = list(map(int, input().split())) # 뽑아내려는 수의 위치
dq = deque([i for i in range(1, n+1)])  # deque([1, 2, 3,...,n])

count = 0   # 2, 3번 연산 (이동) 횟수 세기
for i in position:  # 뽑아내려는 수의 위치 하나씩 반복문 돌리기
    while True:     # 뽑을 때까지 계속 돌리기
        if dq[0] == i:  # 1번 연산 : dq의 첫인덱스가 뽑아내려는 수의 위치와 같다면 뽑아내기
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:  # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 작을때는 왼쪽으로 움직여야 최소
                while dq[0] != i:   # dq의 첫번째 인덱스가 i와 같아질때까지 반복
                    dq.append(dq.popleft())
                    count += 1
            else:   # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 클때는 오른쪽으로 움직여야 최소
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    count += 1
print(count)

