# Perceptrón: Clasificador lineal simple.
# ADALINE (Adaptive Linear Neuron): Usa una función de activación lineal para el aprendizaje.
# MADALINE: Conjunto de ADALINEs organizadas en capas.

class Adaline:
    def __init__(self, n_entradas, tasa_aprendizaje=0.01):
        self.w = [0.0] * (n_entradas + 1) # Pesos + Sesgo
        self.eta = tasa_aprendizaje

    def predecir(self, x):
        # Activación lineal f(z) = z
        z = self.w[0] + sum(xi * wi for xi, wi in zip(x, self.w[1:]))
        return z

    def entrenar(self, x, objetivo):
        # Regla de aprendizaje de Delta (mínimos cuadrados)
        prediccion = self.predecir(x)
        error = objetivo - prediccion
        self.w[1:] = [wi + self.eta * error * xi for wi, xi in zip(self.w[1:], x)]
        self.w[0] += self.eta * error
        return error

ada = Adaline(2)
print(f"Error tras un paso de entrenamiento ADALINE: {ada.entrenar([1, 0], 1)}")