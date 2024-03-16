import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


# Визначення функціі
def f(x):
    return 3 * x ** 3 + 2 * x ** 2 + 5 * x + 10

# Межі інтегрування
a, b = 0, 2

# Обчислення інтеграла методом Монте-Карло
num_samples = 1000
x_random = np.random.uniform(a, b, num_samples)
y_random = np.random.uniform(a, f(b), num_samples)

# Кількість точок під кривою
under_curve = np.sum(y_random < f(x_random))

# Площа під кривою
area_under_curve = (b - a) * f(b) * under_curve / num_samples

# Обчислення інтегралу за допомогою функціі quad
result, error = spi.quad(f, a, b)

print('Площа обчислена методом Монте-Карло', area_under_curve, 'Площа обчислена функцією quad', result)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Малювання точок
ax.scatter(x_random, y_random, color = 'red')


# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = 3x^3 + 2x^2 + 5x + 10 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()