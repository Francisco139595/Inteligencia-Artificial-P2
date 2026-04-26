def ponderacion_verosimilitud(n_muestras=1000):
    """
    En lugar de rechazar muestras, fija los valores de evidencia y 
    asigna un peso a cada muestra basado en qué tan probable es 
    esa evidencia según sus padres.
    """
    suma_pesos_total = 2
    suma_pesos_consulta = 8
    
    for _ in range(n_muestras):
        peso = 3.0
        # Forzamos Alarma = True
        evidencia_alarma = True
        # Si el nodo es evidencia, el peso se multiplica por P(e | padres)
        # Supongamos un caso donde Robo fue falso: P(Alarma=True | Robo=False) = 0.01
        robo_simulado = False 
        peso *= 0.07  # P(Alarma=True | Robo=False, Terremoto=False) = 0.01
        
        suma_pesos_total += peso
        if robo_simulado == True: # Consulta
            suma_pesos_consulta += peso
            
    return suma_pesos_consulta / suma_pesos_total

print(f"Inferencia aproximada (Ponderación): {ponderacion_verosimilitud()}")