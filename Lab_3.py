import random
import numpy as np
from math import sqrt, atan, log2
import matplotlib.pyplot as plt
import time
from datetime import datetime

N = 32  # Кількість точок у сигналі

def generate_signal():
    random.seed(datetime.now().timestamp())  # Ініціалізація генератора випадкових чисел
    signal = []
    for _ in range(N):
        signal.append(random.random())  # Додавання випадкового числа до сигналу
    return signal

def calculate_fft(signal):
    fft_result = np.fft.fft(signal)  # Обчислення швидкого перетворення Фур'є
    amplitudes = [sqrt(c.real**2 + c.imag**2)/2 for c in fft_result]
    phases = [atan(c.imag / c.real) for c in fft_result]
    
    # Розрахунок операцій
    stages = int(log2(N))  # Кількість етапів у FFT
    additions = int(N / 2 * stages * 2)  # Додавання: N/2 комплексних операцій на кожен з stages етапів
    multiplications = int(N / 2 * stages * 4)  # Множення: N/2 комплексних операцій на кожен з stages етапів
    
    return amplitudes, phases, additions, multiplications

def plot_graphs(amplitudes, phases):
    plt.figure(figsize=(10, 6))
    plt.stem(range(N), amplitudes, "b", markerfmt="bo", basefmt=" ", label="|C_k|")
    plt.title("Спектр амплітуд")
    plt.xlabel("k")
    plt.ylabel("Амплітуда")
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.stem(range(N), phases, "b", markerfmt="bo", basefmt=" ", label="arg(C_k)")
    plt.title("Спектр фаз")
    plt.xlabel("k")
    plt.ylabel("Фаза")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    signal = generate_signal()  # Генерація випадкового сигналу
    start = time.time()  # Початок вимірювання часу
    amplitudes, phases, additions, multiplications = calculate_fft(signal)  # Обчислення FFT
    end = time.time()  # Кінець вимірювання часу
    elapsed_time = end - start
    print(f"Час обчислення: {elapsed_time:.10f} секунд")  # Вивід часу з високою точністю
    print(f"Кількість операцій додавання: {additions}")
    print(f"Кількість операцій множення: {multiplications}")
    plot_graphs(amplitudes, phases)

if __name__ == "__main__":
    main()
