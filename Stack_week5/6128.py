from collections import deque
import sys

class MyDeque:
    def __init__(self):
        self.d = deque()

    def push_front(self, x):
        self.d.appendleft(x)
        print("ok")

    def push_back(self, x):
        self.d.append(x)
        print("ok")

    def pop_front(self):
        print(self.d.popleft())

    def pop_back(self):
        print(self.d.pop())

    def front(self):
        print(self.d[0])

    def back(self):
        print(self.d[-1])

    def size(self):
        print(len(self.d))

    def clear(self):
        self.d.clear()
        print("ok")

    def exit(self):
        print("bye")
        sys.exit()

def main():
    dq = MyDeque()
    while True:
        command = input().strip().split()
        if command[0] == "push_front":
            dq.push_front(int(command[1]))
        elif command[0] == "push_back":
            dq.push_back(int(command[1]))
        elif command[0] == "pop_front":
            dq.pop_front()
        elif command[0] == "pop_back":
            dq.pop_back()
        elif command[0] == "front":
            dq.front()
        elif command[0] == "back":
            dq.back()
        elif command[0] == "size":
            dq.size()
        elif command[0] == "clear":
            dq.clear()
        elif command[0] == "exit":
            dq.exit()

if __name__ == "__main__":
    main()
