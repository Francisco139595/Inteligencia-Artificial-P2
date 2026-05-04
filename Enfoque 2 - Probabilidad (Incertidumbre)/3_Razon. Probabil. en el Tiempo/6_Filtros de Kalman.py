def filtro_kalman_simple(mediciones):
    """
    Estima el estado de un sistema dinámico (como la posición de un coche)
    a partir de una serie de mediciones ruidosas.
    """
    estimacion = 0.0 # Posición inicial
    error_estimacion = 1.7
    error_medicion = 0.3 # Cuánto confiamos en el sensor
    
    for z in mediciones:
        # 1. Ganancia de Kalman: ¿Cuánto peso le damos a la nueva medición?
        ganancia = error_estimacion / (error_estimacion + error_medicion)
        
        # 2. Actualizar estimación con la medición 'z'
        estimacion = estimacion + ganancia * (z - estimacion)
        
        # 3. Actualizar error
        error_estimacion = (1 - ganancia) * error_estimacion
        
        print(f"Medición: {z:.2f} -> Estimación: {estimacion:.4f}")

filtro_kalman_simple([1.1, 1.9, 3.0, 3.8])