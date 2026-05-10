import math

class NeuronaEntrenable:
    """
    Implementación del algoritmo de Backpropagation para una sola unidad.
    Este proceso es el corazón del aprendizaje en redes neuronales profundas,
    permitiendo ajustar los pesos basándose en el error de la salida.
    """
    def __init__(self, n_entradas, tasa_aprendizaje=0.1):
        # Inicialización de pesos y sesgo (bias) con valores pequeños
        self.pesos = [0.5] * n_entradas
        self.sesgo = 0.1
        self.eta = tasa_aprendizaje # Tasa de aprendizaje (Learning Rate)

    def sigmoide(self, x):
        """Función de activación para introducir no-linealidad."""
        return 1 / (1 + math.exp(-x))

    def derivada_sigmoide(self, y):
        """
        Derivada de la función sigmoide respecto a su salida.
        Se usa en la regla de la cadena para calcular el gradiente.
        """
        return y * (1 - y)

    def predecir(self, entradas):
        """Paso de alimentación hacia adelante (Forward Pass)."""
        suma_ponderada = sum(x * w for x, w in zip(entradas, self.pesos)) + self.sesgo
        return self.sigmoide(suma_ponderada)

    def entrenar(self, entradas, objetivo):
        """
        Paso de retropropagación (Backward Pass).
        Ajusta los parámetros para minimizar el error cuadrático.
        """
        # 1. Forward Pass: Obtener la predicción actual
        prediccion = self.predecir(entradas)
        
        # 2. Calcular el error (Diferencia entre realidad y predicción)
        error = objetivo - prediccion
        
        # 3. Calcular el Gradiente Local (Delta)
        # Delta = Error * Derivada de la activación
        delta = error * self.derivada_sigmoide(prediccion)
        
        # 4. Actualizar Pesos: W_nuevo = W_anterior + (eta * delta * entrada)
        for i in range(len(self.pesos)):
            self.pesos[i] += self.eta * delta * entradas[i]
            
        # 5. Actualizar Sesgo (Bias)
        self.sesgo += self.eta * delta
        
        return error

# --- PRUEBA DEL ALGORITMO ---
# Intentaremos que la neurona aprenda que la entrada [1, 1] debe dar 1
modelo = NeuronaEntrenable(n_entradas=2, tasa_aprendizaje=0.5)

print("Iniciando entrenamiento por Retropropagación...")
for epoca in range(100):
    error_actual = modelo.entrenar([1, 1], 1.0)
    if epoca % 20 == 0:
        print(f"Época {epoca}: Error = {error_actual:.5f}")

# Resultado final
resultado = modelo.predecir([1, 1])
print(f"\nPredicción final para [1, 1]: {resultado:.4f} (Objetivo: 1.0)")