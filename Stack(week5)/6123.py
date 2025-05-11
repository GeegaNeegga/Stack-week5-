class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        return "ok"

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "error"

    def back(self):
        if self.stack:
            return self.stack[-1]
        return "error"

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()
        return "ok"

    def exit(self):
        return "bye"

stack = Stack()

while True:
    try:
        command = input()
    except EOFError:
        break  # завершить, если конец ввода (например, для автотестов)

    if command.startswith("push"):
        _, n = command.split()
        print(stack.push(int(n)))
    elif command == "pop":
        print(stack.pop())
    elif command == "back":
        print(stack.back())
    elif command == "size":
        print(stack.size())
    elif command == "clear":
        print(stack.clear())
    elif command == "exit":
        print(stack.exit())
        break
