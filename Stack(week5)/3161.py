from collections import deque
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    
    deques = {}  # Словарь для хранения деков по номерам A
    result = []
    
    for line in data[1:]:
        command = line.split()
        if command[0] == 'pushfront':
            A = int(command[1])
            B = int(command[2])
            if A not in deques:
                deques[A] = deque()
            deques[A].appendleft(B)
        elif command[0] == 'pushback':
            A = int(command[1])
            B = int(command[2])
            if A not in deques:
                deques[A] = deque()
            deques[A].append(B)
        elif command[0] == 'popfront':
            A = int(command[1])
            result.append(str(deques[A].popleft()))
        elif command[0] == 'popback':
            A = int(command[1])
            result.append(str(deques[A].pop()))
    
    # Выводим все результаты за один раз
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()
