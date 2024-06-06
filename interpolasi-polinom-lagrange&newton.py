banner = """
====================================================
||    Interpolasi Polinom Lagrange dan Newton     ||
||                                                ||
||             Rizky Ananta Fadhila               ||
||                21120122120029                  ||
====================================================
"""

print(banner)

import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Polinom Lagrange
def lagrange_interpolation(x, y, xp):
    yp = 0
    for i in range(len(x)):
        p = 1
        for j in range(len(x)):
            if i != j:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += p * y[i]
    return yp

# Polinom Newton
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    return coef[0, :]

def newton_interpolation(x, y, xp):
    coef = divided_diff(x, y)
    n = len(x) - 1
    yp = coef[n]
    for k in range(1, n + 1):
        yp = coef[n - k] + (xp - x[n - k]) * yp
    return yp

# Plot
x_plot = np.linspace(5, 40, 100)
y_lagrange = [lagrange_interpolation(x, y, i) for i in x_plot]
y_newton = [newton_interpolation(x, y, i) for i in x_plot]

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, y, 'ro', label='Data')
plt.plot(x_plot, y_lagrange, 'b-', label='Lagrange Interpolation')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, y, 'ro', label='Data')
plt.plot(x_plot, y_newton, 'g--', label='Newton Interpolation')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()