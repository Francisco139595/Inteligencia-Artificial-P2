class RedBayesiana:
    """
    Representa una estructura de Red Bayesiana simple.
    Relaciona variables aleatorias mediante dependencias directas.
    """
    def __init__(self):
        # Nodos representados como: {Variable: [Padres]}
        self.grafo = {}
        # Tablas de Probabilidad Condicional (CPT)
        self.cpt = {}

    def agregar_nodo(self, variable, padres, tabla):
        """
        Define un nodo, sus dependencias (padres) y su CPT.
        """
        self.grafo[variable] = padres
        self.cpt[variable] = tabla

# Ejemplo de uso: Modelo de Robo (A) que activa una Alarma (B)
red = RedBayesiana()
# P(Robo) = 0.001 (Nodo raíz)
red.agregar_nodo("Robo", [], {tuple(): 0.001})
# P(Alarma | Robo) = 0.95, P(Alarma | No Robo) = 0.01
red.agregar_nodo("Alarma", ["Robo"], {(True,): 0.95, (False,): 0.01})

print("Red Bayesiana definida exitosamente.")