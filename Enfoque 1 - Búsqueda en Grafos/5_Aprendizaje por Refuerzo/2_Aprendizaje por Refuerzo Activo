import random

class AgenteActivo:
    """
    Un agente activo interactúa con el entorno, actualiza sus creencias
    y decide su próxima acción basándose en lo aprendido.
    """
    def __init__(self, estados, acciones):
        self.U = {s: 0.0 for s in estados} # Utilidades estimadas
        self.N = {s: 0 for s in estados}   # Contador de visitas
        self.acciones = acciones

    def actualizar_utilidad(self, estado, recompensa, sig_estado, gamma=0.9, alpha=0.1):
        """
        Usa la diferencia temporal (TD Learning) para actualizar utilidades:
        U(s) = U(s) + alpha * [R(s) + gamma * U(s') - U(s)]
        """
        self.N[estado] += 1
        # El error de predicción (TD Error) es lo que está dentro de los corchetes
        error = recompensa + (gamma * self.U[sig_estado]) - self.U[estado]
        self.U[estado] += alpha * error

# Ejemplo de inicialización
agente = AgenteActivo(["Inicio", "Camino", "Meta"], ["Norte", "Sur"])
print("Agente activo inicializado para explorar y aprender.")