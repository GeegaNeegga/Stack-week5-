def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '['}
    for char in s:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if not stack or stack[-1] != pairs[char]:
                return "No"
            stack.pop()
    return "Yes" if not stack else "No"

n = int(input())
for _ in range(n):
    expr = input().strip()
    print(is_balanced(expr))