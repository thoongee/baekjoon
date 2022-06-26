import sys
input = sys.stdin.readline

N = int(input())
mid = 10
deque = []
head = mid # 0~
tail = mid

for _ in range(N):

    command = list(input().split())

    if command[0]== 'push_front':
        deque.insert(head,int(command[1])) # insert(index, 값)
        head -= 1

    if command[0]== 'push_back':
        deque.insert(tail, int(command[1]))
        tail += 1

    if command[0]=='pop_front':
        if head == tail:
            print(-1)
        else:
            head += 1
            print(deque[head-1])
            del deque[head-1] # pos만 옮겨주면 되는줄

    if command[0]=='pop_back':
        if head == tail:
            print(-1)
        else:
            tail -= 1
            print(deque[tail])
            del deque[tail] # pos만 옮겨주면 되는줄

    if command[0]=='size':
        print(tail-head)

    if command[0]=='empty':
        if head == tail:
            print(1)
        else:
            print(0)

    if command[0] == 'front':
        if head == tail:
            print(-1)
        else:
            print(deque[head])

    if command[0] == 'back':
        if head == tail:
            print(-1)
        else:
            print(deque[tail-1])


