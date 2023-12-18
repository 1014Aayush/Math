import numpy as np
from scipy.interpolate import lagrange


x_values = np.array([0, 0.4, 0.9, 1.2, 1.5])
y_values = np.array([1, 1.8556, 2.5868, 2.1786, 0.4167])

def divided_differences(x, y):
    n = len(y)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (x[i + j] - x[i])
            print(table[i,j])

    return table

def interpolate_newton(x, y, value, table):
    result = table[0, 0]
    product = 1

    for i in range(1, len(x)):
        product *= (value - x[i - 1])
        print(product)
        result += table[0, i] * product
        print(result)

    return result

table = divided_differences(x_values, y_values)
result = interpolate_newton(x_values, y_values, 0.7, table)
print(result)






# Using Lagrange interpolation
x_values = [0, 0.4, 0.9, 1.2, 1.5]
y_values = [1, 1.8556, 2.5868, 2.1786, 0.4167]
poly = lagrange(x_values, y_values)
result = poly(0.7)
print(result)