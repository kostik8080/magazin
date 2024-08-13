def generate_sequence(n):
    sequence = []
    for i in range(1, n + 1):
        sequence.extend([i] * i)  # Добавляем число i, i раз
        if len(sequence) >= n:  # Проверяем, не превышает ли длина n
            break
    return sequence[:n]  # Возвращаем только первые n элементов


# Пример использования
n = int(input("Введите количество элементов последовательности: "))
result = generate_sequence(n)
print(*result)
