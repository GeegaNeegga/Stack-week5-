from collections import deque

def main():
    # Чтение числа операций
    n = int(input())
    
    # Инициализация дека для хранения книг
    shelf = deque()
    
    # Обработка операций
    for _ in range(n):
        operation = list(map(int, input().split()))
        
        if operation[0] == 1:  # Добавление книги слева
            shelf.appendleft(operation[1])
        elif operation[0] == 2:  # Добавление книги справа
            shelf.append(operation[1])
        elif operation[0] == 3:  # Снятие книги слева
            print(shelf.popleft())
        elif operation[0] == 4:  # Снятие книги справа
            print(shelf.pop())

if __name__ == "__main__":
    main()
