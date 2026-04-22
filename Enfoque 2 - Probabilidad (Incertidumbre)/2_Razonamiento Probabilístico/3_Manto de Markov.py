from typing import Any

def obtener_manto_markov(red: Any, nodo: str) -> dict:
    """
    El Manto de Markov de un nodo incluye sus padres, sus hijos y 
    los otros padres de sus hijos. Es el conjunto mínimo de nodos que 
    hacen a un nodo independiente del resto de la red.
    """
    if not hasattr(red, 'grafo') or not isinstance(red.grafo, dict):
        raise TypeError("El objeto 'red' debe tener un atributo 'grafo' que sea un diccionario.")

    padres = set(red.grafo.get(nodo, []))
    hijos = set()
    copadres = set()
    
    for n, padres_n in red.grafo.items():
        if nodo in padres_n:
            hijos.add(n) # Es un hijo
            # Agregar otros padres del hijo (copadres)
            for p in padres_n:
                if p != nodo:
                    copadres.add(p)
                    
    return {"Padres": padres, "Hijos": hijos, "Copadres": copadres}

# Clase de prueba para simular la red bayesiana y evitar un NameError
class RedSimulada:
    def __init__(self):
        # Formato del grafo: {Hijo: [Padres]}
        self.grafo = {
            "Robo": [],
            "Terremoto": [],
            "Alarma": ["Robo", "Terremoto"]
        }

red = RedSimulada()

# Usando la lógica de la red anterior
manto = obtener_manto_markov(red, "Robo")
print(f"Manto de Markov de 'Robo': {manto}")