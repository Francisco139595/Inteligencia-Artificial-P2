import random

def gibbs_sampling(iteraciones: int = 1000) -> float:
    """
    Genera una secuencia de estados (Cadena de Markov) donde cada estado 
    depende del anterior. Muestrea cada variable condicionada a su Manto de Markov.
    """
    if iteraciones <= 0:
        raise ValueError("El número de iteraciones debe ser mayor a cero.")
        
    # Estado inicial aleatorio
    estado = {"Robo": False, "Alarma": True, "JuanLlamó": True}
    conteo_consulta = 0
    
    for _ in range(iteraciones):
        # Elegir una variable que no sea evidencia para actualizar
        # Actualizamos 'Robo' basándonos en sus vecinos actuales
        prob_robo_condicionada = 0.02 # Valor hipotético P(Robo | Manto)
        estado["Robo"] = random.random() < prob_robo_condicionada
        
        if estado["Robo"]:
            conteo_consulta += 1
            
    return conteo_consulta / iteraciones

print(f"Inferencia mediante MCMC (Gibbs): {gibbs_sampling()}")