from collections import deque

def solve(n, current_order, ideal_order):
    time = 0
    current_queue = deque(current_order)
    ideal_queue = deque(ideal_order)

    # Пока очередь не пуста
    while current_queue:
        # Если первый процесс совпадает с идеальным порядком, выполняем его
        if current_queue[0] == ideal_queue[0]:
            current_queue.popleft()  # Удаляем процесс из очереди
            ideal_queue.popleft()    # Удаляем из идеального порядка
            time += 1                # Затрачено 1 единицу времени
        else:
            # Если не совпадает, перемещаем процесс в конец очереди
            current_queue.append(current_queue.popleft())
            time += 1                # Затрачено 1 единицу времени

    return time

def main():
    n = int(input())  # Количество процессов
    if n == 0:
        return
    current_order = list(map(int, input().split()))  # Порядок вызова процессов
    ideal_order = list(map(int, input().split()))    # Идеальный порядок выполнения
    result = solve(n, current_order, ideal_order)
    print(result)

if __name__ == "__main__":
    main()
