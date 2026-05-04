def demostracion_tareas_temporales(tiempo_actual: int = 3, pasos_futuros: int = 2) -> None:
    """
    Conceptos clave en razonamiento temporal (ej. Modelos Ocultos de Markov):
    1. Filtrado: Estimar el estado actual dada la evidencia pasada y presente.
    2. Predicción: Estimar estados futuros.
    3. Suavizado: Re-estimar estados pasados con evidencia nueva (mejor que el filtrado).
    4. Explicación: Hallar la secuencia de estados más probable (Algoritmo de Viterbi).
    """
    print("--- Tareas de Inferencia en Modelos Temporales ---")
    print(f"Evidencia recolectada hasta t={tiempo_actual}: [e_1, e_2, ..., e_{tiempo_actual}]\n")
    
    # 1. Filtrado: Útil para rastrear el estado actual (ej. ¿dónde está el robot hoy basándose en sus sensores?)
    print(f"1. Filtrado: P(X_{tiempo_actual} | e_1:{tiempo_actual})")
    print(f"   -> ¿Cuál es el estado del sistema HOY (t={tiempo_actual}) dado lo observado?\n")
    
    # 2. Predicción: Útil para anticipar eventos sin tener nueva evidencia (ej. ¿lloverá en 3 días?)
    print(f"2. Predicción: P(X_{tiempo_actual + pasos_futuros} | e_1:{tiempo_actual})")
    print(f"   -> ¿Cuál será el estado en el FUTURO (t={tiempo_actual + pasos_futuros})?\n")
    
    # 3. Suavizado (Smoothing): Mejora las estimaciones pasadas al usar "evidencia futura" relativa
    print(f"3. Suavizado: P(X_{tiempo_actual - 1} | e_1:{tiempo_actual})")
    print(f"   -> En retrospectiva, ¿cuál fue el estado AYER (t={tiempo_actual - 1}) sabiendo la evidencia de hoy?\n")
    
    # 4. Explicación: Busca la trayectoria completa más probable (ej. procesar oraciones en reconocimiento de voz)
    print(f"4. Explicación (Viterbi): argmax P(X_1:{tiempo_actual} | e_1:{tiempo_actual})")
    print(f"   -> ¿Cuál fue la HISTORIA más probable de estados desde t=1 hasta t={tiempo_actual}?\n")

# Ejecución de la demostración en el tiempo t=5, prediciendo 3 pasos hacia adelante (t=8)
demostracion_tareas_temporales(tiempo_actual=5, pasos_futuros=3)
