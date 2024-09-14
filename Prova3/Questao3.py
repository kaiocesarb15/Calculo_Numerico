import numpy as np

# Constantes do problema
b = 2.9e-2  # taxa de nascimento
k = 1.4e-7  # constante de mortalidade
P0 = 50976  # população inicial
t_final = 5  # anos
h = 0.1  # passo (tamanho do intervalo)

# Função que define a EDO dP/dt
def dP_dt(t, P):
    return b * P - k * P**2

# Método de Runge-Kutta de 4ª ordem
def runge_kutta_4(dP_dt, P0, t_final, h):
    t_values = np.arange(0, t_final + h, h)
    P_values = np.zeros(len(t_values))
    P_values[0] = P0
    
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        P = P_values[i-1]
        
        k1 = h * dP_dt(t, P)
        k2 = h * dP_dt(t + h/2, P + k1/2)
        k3 = h * dP_dt(t + h/2, P + k2/2)
        k4 = h * dP_dt(t + h, P + k3)
        
        P_values[i] = P + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return t_values, P_values

# Resolver a EDO
t_values, P_values = runge_kutta_4(dP_dt, P0, t_final, h)

# Exibir a população após 5 anos
populacao_final = P_values[-1]
print(f"População estimada após 5 anos: {populacao_final:.2f} indivíduos")
