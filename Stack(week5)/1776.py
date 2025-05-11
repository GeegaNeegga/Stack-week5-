import sys

input = sys.stdin.read
lines = input().splitlines()

i = 0
while True:
    n = int(lines[i])
    if n == 0:
        break
    i += 1
    while True:
        line = lines[i]
        i += 1
        if line == "0":
            print()
            break
        target = list(map(int, line.split()))
        stack = []
        current = 1
        possible = True
        for num in target:
            while current <= n and (not stack or stack[-1] != num):
                stack.append(current)
                current += 1
            if stack and stack[-1] == num:
                stack.pop()
            else:
                possible = False
                break
        print("Yes" if possible else "No")
