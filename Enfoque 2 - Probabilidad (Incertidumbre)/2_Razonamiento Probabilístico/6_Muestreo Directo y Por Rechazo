import random

def muestreo_rechazo(red, consulta, evidencia, n_muestras=1000):
    """
    Genera muestras de la red y descarta aquellas que no coinciden 
    con la evidencia observada.
    """
    muestras_validas = 0
    muestras_consulta_positiva = 0

    for _ in range(n_muestras):
        # Simular Robo (P=0.001)
        robo = random.random() < 0.001
        # Simular Alarma basado en Robo
        prob_alarma = 0.95 if robo else 0.01
        alarma = random.random() < prob_alarma
        
        # Filtro de Rechazo: ¿Coincide con la evidencia?
        # Supongamos evidencia: Alarma = True
        if alarma == evidencia["Alarma"]:
            muestras_validas += 1
            if robo == consulta["Robo"]:
                muestras_consulta_positiva += 1
                
    if muestras_validas == 0: return 0
    return muestras_consulta_positiva / muestras_validas

print(f"Probabilidad por Muestreo de Rechazo: {muestreo_rechazo(None, {'Robo': True}, {'Alarma': True})}")