import math

class Neurona:
    """
    Base del Deep Learning: Una neurona (Perceptrón) con función de activación.
    """
    def __init__(self, n_entradas):
        self.pesos = [0.5] * n_entradas
        self.sesgo = 0.1

    def activar(self, x):
        # Suma ponderada: z = sum(w*x) + b
        z = sum(w * xi for w, xi in zip(self.pesos, x)) + self.sesgo
        # Función Sigmoide: 1 / (1 + e^-z)
        return 1 / (1 + math.exp(-z))

# Capa de entrada de 3 neuronas
mi_neurona = Neurona(3)
print(f"Salida de la neurona: {mi_neurona.activar([1.0, 0.5, -0.2]):.4f}")