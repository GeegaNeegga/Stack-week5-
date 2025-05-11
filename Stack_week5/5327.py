n = int(input())
stack = []

for _ in range(n):
    parts = input().split()
    if parts[0] == '1':
        stack.append(int(parts[1]))
    else:
        print(stack.pop())
