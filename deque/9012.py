import sys
input = sys.stdin.readline

T = int(input())

# 스택이용
for i in range(T):
    stack = []
    a=input().strip()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop() # stack에 (가 있으면 pop
            else: # 스택에 괄호가 없을경우
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됐을경우
        if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
            print("NO")

            
# sum 이용
