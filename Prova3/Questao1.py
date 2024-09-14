import numpy as np

# Definindo a função f(x, y) = y' = (y^2 - 2x) / y
def f(x, y):
    return (y**2 - 2*x) / y

# Método de Euler
def euler_method(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
    return y

# Método de Runge-Kutta de 3ª ordem
def runge_kutta_3(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h, y - h * k1 + 2 * h * k2)
        y = y + (h/6) * (k1 + 4*k2 + k3)
        x = x + h
    return y

# Solução exata
def exact_solution(x):
    return np.sqrt(2*x + 1)

# Parâmetros iniciais
x0 = 0
y0 = 1
h = 0.2
n = int(1 / h)  # Número de passos para x = 1

# Aproximação pelo método de Euler
y_euler = euler_method(f, x0, y0, h, n)

# Aproximação pelo método de Runge-Kutta de 3ª ordem
y_runge_kutta = runge_kutta_3(f, x0, y0, h, n)

# Valor exato de y(1)
y_exact = exact_solution(1)

# Cálculo do erro absoluto
error_euler = abs(y_exact - y_euler)
error_runge_kutta = abs(y_exact - y_runge_kutta)

# Exibição dos resultados
print(f"Aproximação de y(1) pelo método de Euler: {y_euler:.5f}")
print(f"Aproximação de y(1) pelo método de Runge-Kutta de 3ª ordem: {y_runge_kutta:.5f}")
print(f"Valor exato de y(1): {y_exact:.5f}")
print(f"Erro absoluto do método de Euler: {error_euler:.5f}")
print(f"Erro absoluto do método de Runge-Kutta de 3ª ordem: {error_runge_kutta:.5f}")
