import numpy as np

def entrenar_q_learning(pasos=100, alpha=0.1, gamma=0.9, epsilon=0.1):
    # Definimos el espacio: 3 estados y 2 acciones (Izquierda=0, Derecha=1)
    # El objetivo es llegar al estado 2 (recompensa +10)
    q_table = np.zeros((3, 2))
    estado_actual = 0
    for _ in range(pasos):
        # 1. Selección de acción (Epsilon-Greedy)
        if np.random.uniform(0, 1) < epsilon:
            accion = np.random.choice([0, 1]) # Explorar
        else:
            accion = np.argmax(q_table[estado_actual]) # Explotar (mejor acción)

        # 2. Simulación de la transición (Mundo simplificado)
        nuevo_estado = min(2, estado_actual + 1) if accion == 1 else max(0, estado_actual - 1)
        recompensa = 10 if nuevo_estado == 2 else -1
        
        # 3. ACTUALIZACIÓN Q (Ecuación de Bellman para Q-Learning)
        # Q(s,a) = Q(s,a) + alpha * [R + gamma * max(Q(s',a')) - Q(s,a)]
        # Para el estado terminal (2), el valor futuro esperado debe ser 0 explícitamente
        mejor_q_s_sig = np.max(q_table[nuevo_estado]) if nuevo_estado != 2 else 0
        q_table[estado_actual, accion] += alpha * (recompensa + gamma * mejor_q_s_sig - q_table[estado_actual, accion])
        
        estado_actual = nuevo_estado if nuevo_estado != 2 else 0
        
    return q_table

q_table_final = entrenar_q_learning(2000)
print("Matriz Q resultante (Estado x Acción):\n", q_table_final)

# Extracción e impresión de la Política Óptima
print("\nPolítica Óptima Inferida:")
acciones_texto = {0: "Izquierda", 1: "Derecha"}
for estado in range(2): # Solo evaluamos los estados no terminales (0 y 1)
    mejor_accion = np.argmax(q_table_final[estado])
    print(f"Estado {estado} -> Mover a la {acciones_texto[int(mejor_accion)]}")