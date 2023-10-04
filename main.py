import math
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def centerEquippingIntegral(f, a, b, n):
    """
    Вычисляет приближенное значение определенного интеграла функции на отрезке [a, b]
    с использованием метода центральных прямоугольников с n интервалами.

    f: функция, которую нужно проинтегрировать
    a: начало отрезка
    b: конец отрезка
    n: количество интервалов

    Возвращает приближенное значение определенного интеграла и погрешность.
    """
    delta_x = (b - a) / n  # длина интервала
    x = np.linspace(a + delta_x / 2, b - delta_x / 2, n)  # середины интервалов
    y = f(x)  # значения функции в серединах интервалов
    integral = np.sum(y * delta_x)  # приближенное значение интеграла
    error = np.abs(integral - spi.quad(f, a, b)[0])  # погрешность
    return integral, x, y, error

def rightEquippingIntegral(f, a, b, n):
    delta_x = (b - a) / n  # длина интервала
    x = np.linspace(a + delta_x, b - delta_x, n)  # середины интервалов
    y = f(x)  # значения функции в серединах интервалов
    integral = np.sum(y * delta_x)  # приближенное значение интеграла
    error = np.abs(integral - spi.quad(f, a, b)[0])  # погрешность
    return integral, x, y, error

def leftEquippingIntegral(f, a, b, n):
    delta_x = (b - a) / n  # длина интервала
    x = np.linspace(a, b, n+1)  # середины интервалов
    y = f(x)  # значения функции в серединах интервалов
    integral = np.sum(y * delta_x)  # приближенное значение интеграла
    error = np.abs(integral - spi.quad(f, a, b)[0])  # погрешность
    return integral, x, y, error



print("Выберите тип оснащения: ")
print("1) левые")
print("2) средние")
print("3) правые")
equip = int(input())

print("Введите количество точек разбиения: ")
n = int(input())  # количество точек разбиения
a = 1
b = 2
f = lambda x: math.e**(-2*x)
fig, ax = plt.subplots()

if equip == 2:
    I, x, y, e = centerEquippingIntegral(f, a, b, n)
    # для средних оснащений
    ax.plot()
    x0 = a  # координата начала прямоугольника
    for i in range(n):
        ax.add_patch(Rectangle((x0, 0), 2 * (x[i] - x0), y[i]))
        x0 += 2 * (x[i] - x0)

elif equip == 1:
    I, x, y, e = leftEquippingIntegral(f, a, b, n)
    # для левых оснащений
    ax.plot()
    x0 = a  # координата начала прямоугольника
    for i in range(n):
        if i == n-1:
            ax.add_patch(Rectangle((x0, 0), b - x0, y[i]))
        else:
            ax.add_patch(Rectangle((x0, 0), x[i+1] - x0, y[i]))
            x0 = x[i+1]

else:
    I, x, y, e = rightEquippingIntegral(f, a, b, n)
    # для правых оснащений
    ax.plot()
    x0 = a  # координата начала прямоугольника
    for i in range(n):
        ax.add_patch(Rectangle((x0, 0), x[i] - x0, y[i]))
        x0 = x[i]

plt.show()
print("Интеграл: ", I)
print("Ошибка: ", e)

