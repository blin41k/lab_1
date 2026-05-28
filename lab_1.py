import time
import matplotlib.pyplot as plt

def is_empty(stack):
    return len(stack) == 0

sizes = [0, 1, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
times = []

print("Размер стека | Время")

for size in sizes:
    stack = [1] * size

    start_time = time.time()

    for _ in range(1000000):
        is_empty(stack)

    end_time = time.time()

    execution_time = end_time - start_time
    times.append(execution_time)

    print(size, "|", execution_time)

plt.plot(sizes, times, marker='o')
plt.title("Проверка пустоты стека")
plt.xlabel("Количество элементов")
plt.ylabel("Время выполнения, с")
plt.grid(True)
plt.show()