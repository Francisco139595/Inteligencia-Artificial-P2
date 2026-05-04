from typing import Dict, List

def forward_backward(prob_inicial: Dict[str, float], transiciones: Dict[str, Dict[str, float]], modelo_sensor: Dict[str, Dict[str, float]], secuencia_obs: List[str]) -> str:
    """
    Algoritmo Hacia Delante-Atrás (Forward-Backward) para suavizado en HMM. 
    Calcula la probabilidad exacta de cada estado en cada paso de tiempo k (1 <= k <= t)
    dada TODA la secuencia de observaciones hasta t.
    """
    t = len(secuencia_obs)
    print("--- Iniciando Algoritmo Forward-Backward ---")
    print(f"Secuencia de observaciones (t={t}): {secuencia_obs}\n")
    
    # Forward: calcula P(X_k | e_1:k) 
    # -> Representa la probabilidad de estar en un estado usando solo la información hasta ese momento.
    print("Paso 1 (Forward / Hacia Delante):")
    print("  -> Filtrando desde el inicio hasta el tiempo t.")
    print("  -> Calculando probabilidades de los estados dados los datos hasta cada instante.\n")
    
    # Backward: calcula P(e_k+1:t | X_k) 
    # -> Representa la probabilidad de observar el resto de la secuencia futura dado el estado actual.
    print("Paso 2 (Backward / Hacia Atrás):")
    print("  -> Propagando la evidencia futura desde t hacia el inicio.")
    print("  -> Calculando la probabilidad de las observaciones futuras dado el estado actual.\n")
    
    # Suavizado: P(X_k | e_1:t) = alpha * Forward * Backward
    print("Paso 3 (Suavizado / Combinación):")
    print("  -> Multiplicando el mensaje Forward (pasado/presente) con el mensaje Backward (futuro).")
    print("  -> Normalizando para obtener la distribución suavizada final P(X_k | e_1:t).\n")
    
    return "-> Resultado: Distribución de probabilidad suavizada para cada paso de tiempo."

# --- Simulación con un Modelo Oculto de Markov (HMM) Clásico ---
# Variables ocultas (X): Clima (Sol, Lluvia) -> Lo que queremos descubrir.
# Observaciones (e): Paraguas (Sí, No) -> La evidencia que podemos ver (nuestro sensor).

# Distribución de probabilidad inicial (Día 0)
prob_inicial_clima = {"Sol": 0.5, "Lluvia": 0.5}

# Modelo de Transición: ¿Cómo cambia el clima de un día para otro? (Dinámica del sistema)
modelo_transicion = {
    "Sol": {"Sol": 0.7, "Lluvia": 0.3},
    "Lluvia": {"Sol": 0.3, "Lluvia": 0.7}
}

# Modelo del Sensor (Emisión): ¿Qué tan probable es ver un paraguas dado el clima real?
modelo_sensor_paraguas = {
    "Sol": {"Paraguas_Sí": 0.2, "Paraguas_No": 0.8},
    "Lluvia": {"Paraguas_Sí": 0.9, "Paraguas_No": 0.1}
}

# Evidencia empírica recolectada a lo largo del tiempo (Día 1, Día 2, Día 3)
observaciones_dias = ["Paraguas_Sí", "Paraguas_Sí", "Paraguas_No"]

resultado = forward_backward(prob_inicial_clima, modelo_transicion, modelo_sensor_paraguas, observaciones_dias)
print(resultado)
