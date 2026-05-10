import random

def som_paso(pesos_neuronas, entrada, tasa_apren=0.1):
    """
    Aprendizaje No Supervisado: Las neuronas compiten para representar 
    patrones de entrada. La neurona más cercana (BMU) se actualiza.
    """
    # 1. Encontrar la neurona ganadora (distancia mínima)
    distancias = [sum((w - e)**2 for w, e in zip(neurona, entrada)) for neurona in pesos_neuronas]
    ganadora_idx = distancias.index(min(distancias))
    
    # 2. Actualizar pesos de la neurona ganadora para que se parezca más a la entrada
    for i in range(len(pesos_neuronas[ganadora_idx])):
        pesos_neuronas[ganadora_idx][i] += tasa_apren * (entrada[i] - pesos_neuronas[ganadora_idx][i])
        
    return ganadora_idx

red_kohonen = [[0.1, 0.1], [0.9, 0.9]] # Dos neuronas
print(f"Índice de la neurona ganadora: {som_paso(red_kohonen, [0.8, 0.85])}")