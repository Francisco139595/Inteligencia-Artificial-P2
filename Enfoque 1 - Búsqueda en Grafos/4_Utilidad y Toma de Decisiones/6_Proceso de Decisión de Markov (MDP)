class MDP:
    """
    Clase que encapsula los componentes de un Proceso de Decisión de Markov.
    """
    def __init__(self, estados, acciones, transiciones, recompensas, gamma=0.9):
        self.estados = estados
        self.acciones = acciones
        self.transiciones = transiciones # P(s' | s, a)
        self.recompensas = recompensas
        self.gamma = gamma

    def obtener_recompensa(self, estado):
        return self.recompensas.get(estado, 0)

# Ejemplo de instancia de MDP
mi_mdp = MDP(["S1", "S2"], ["Ir"], {"S1": {"Ir": [("S2", 1.0)]}}, {"S2": 5})
print(f"MDP inicializado con factor de descuento: {mi_mdp.gamma}")