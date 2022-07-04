import sys
input = sys.stdin.readline

T = int(input())

# 스택이용
# 괄호 갯수가 맞으면 VPS인줄 알았다

for i in range(T):
    stack = []
    line = input().strip()
    for item in line:
        if stack:
            if item =='(':
                stack.append(item)
            elif item==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(item)

        else:
            stack.append(item)

    if stack: # stack에 괄호가 남아있다면
        print("NO")
    else:
        print("YES")
            
# sum 이용
