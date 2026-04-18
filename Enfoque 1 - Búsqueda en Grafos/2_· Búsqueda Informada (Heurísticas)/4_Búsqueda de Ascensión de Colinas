import random

def funcion_objetivo(x):
    """Función a optimizar: f(x) = -(x-3)^2 + 15. El máximo real es x=3."""
    return -((x - 3)**2) + 15

def hill_climbing(pasos=1000):
    # 1. Punto de partida aleatorio
    actual = random.uniform(-10, 10)
    valor_actual = funcion_objetivo(actual)
    
    for _ in range(pasos):
        # 2. Generar un vecino muy cercano (movimiento pequeño)
        vecino = actual + random.uniform(-0.1, 0.1)
        valor_vecino = funcion_objetivo(vecino)
        
        # 3. Si el vecino es mejor, nos movemos a esa posición
        if valor_vecino > valor_actual:
            actual = vecino
            valor_actual = valor_vecino
            
    return actual, valor_actual

x_opt, f_opt = hill_climbing()
print(f"Máximo local encontrado en x: {x_opt:.2f}, Valor f(x): {f_opt:.2f}")