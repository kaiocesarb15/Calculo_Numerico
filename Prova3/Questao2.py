import numpy as np

# Função que define a EDO dv/dt
def dv_dt(v):
    return g - (k / m) * v * abs(v)

# Método de Euler para resolver a EDO
def euler_method(v0, h, t_final):
    t_values = np.arange(0, t_final + h, h)
    v_values = np.zeros(len(t_values))
    v_values[0] = v0
    
    for i in range(1, len(t_values)):
        v_values[i] = v_values[i-1] + h * dv_dt(v_values[i-1])
    
    return t_values, v_values

# Encontrar o tempo em que o projétil começa a cair
def find_time_to_fall(v0, h):
    t = 0
    v = v0
    while v > 0:
        v = v + h * dv_dt(v)
        t += h
    return t

# Constantes
m = 0.11  # massa (kg)
g = -9.8  # gravidade (m/s^2)
k = 0.002  # coeficiente de resistência do ar (kg/m)
v0 = 8.0  # velocidade inicial (m/s)
h = 0.1  # intervalo de tempo (s)
t_final = 1.0  # tempo final (s)

# Resolver a EDO
t_values, v_values = euler_method(v0, h, t_final)

# Exibir os resultados
for t, v in zip(t_values, v_values):
    print(f"Tempo: {t:.1f}s, Velocidade: {v:.5f} m/s")

# Tempo em que o projétil começa a cair
time_to_fall = find_time_to_fall(v0, h)
print(f"O projetil começa a cair após {time_to_fall:.2f} segundos")
