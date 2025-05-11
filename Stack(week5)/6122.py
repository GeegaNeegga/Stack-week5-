class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        print("ok")

    def pop(self):
        print(self.stack.pop())

    def back(self):
        print(self.stack[-1])

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack.clear()
        print("ok")

    def exit(self):
        print("bye")
        return False  # сигнал к выходу

stack = Stack()

while True:
    command = input()
    if command.startswith("push"):
        _, n = command.split()
        stack.push(int(n))
    elif command == "pop":
        stack.pop()
    elif command == "back":
        stack.back()
    elif command == "size":
        stack.size()
    elif command == "clear":
        stack.clear()
    elif command == "exit":
        if not stack.exit():
            break
