from collections import deque

def solve(n):
    # Инициализируем колоду карт от 1 до n
    deck = deque(range(1, n + 1))
    discarded = []

    # Пока в колоде больше одной карты
    while len(deck) > 1:
        discarded.append(deck.popleft())  # Выбросить верхнюю карту
        deck.append(deck.popleft())  # Переместить верхнюю карту в конец

    # Вывести результат
    print(" ".join(map(str, discarded)))  # Выбрасываемые карты
    print(deck[0])  # Оставшаяся карта

def main():
    while True:
        n = int(input())  # Чтение количества карт
        if n == 0:
            break
        solve(n)

if __name__ == "__main__":
    main()
