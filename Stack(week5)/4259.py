import sys

input = sys.stdin.read
data = input().split()

stack = []
output = []

i = 1  # Начинаем после числа n
n = int(data[0])

while i < len(data):
    t = int(data[i])
    
    if t == 1:
        x = int(data[i + 1])
        if stack:
            current_min = min(x, stack[-1][1])
        else:
            current_min = x
        stack.append((x, current_min))
        i += 2
    elif t == 2:
        stack.pop()
        i += 1
    elif t == 3:
        output.append(str(stack[-1][1]))
        i += 1

print("\n".join(output))
