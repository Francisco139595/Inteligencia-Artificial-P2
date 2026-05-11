import collections
import random
from typing import List

class ModeloBigramas:
    """
    Un modelo de lenguaje basado en Bigramas (N=2).
    Estima la probabilidad de que una palabra siga a otra basándose en un corpus de texto.
    
    Aplica la Suposición de Markov: "El futuro (la siguiente palabra) depende 
    SOLO del presente (la palabra actual), no de todo el pasado".
    """
    def __init__(self, corpus: str):
        # 1. Limpieza y tokenización simple
        self.palabras = corpus.lower().split()
        
        # 2. Construcción de Bigramas (Pares de palabras consecutivas)
        # Ejemplo: ["el", "gato", "come"] -> [("el", "gato"), ("gato", "come")]
        self.bigramas = [(self.palabras[i], self.palabras[i+1]) for i in range(len(self.palabras)-1)]
        
        # 3. Conteo de frecuencias (usamos Counter para un conteo altamente optimizado)
        self.frecuencias_bigramas = collections.Counter(self.bigramas)
        self.frecuencias_unigramas = collections.Counter(self.palabras)
        
    def probabilidad(self, w1: str, w2: str) -> float:
        """
        Calcula la probabilidad condicional P(w2 | w1).
        Fórmula matemática: P(w2 | w1) = Count(w1, w2) / Count(w1)
        """
        total_w1 = self.frecuencias_unigramas.get(w1, 0)
        if total_w1 == 0: 
            return 0.0 # La palabra w1 nunca se vio en el entrenamiento
            
        ocurrencias_w1_w2 = self.frecuencias_bigramas.get((w1, w2), 0)
        return ocurrencias_w1_w2 / total_w1

    def generar_texto(self, semilla: str, longitud: int = 5) -> str:
        """
        Usa las probabilidades aprendidas para predecir y generar nuevo texto.
        Esto es la base conceptual de modelos generativos como ChatGPT.
        """
        texto_generado = [semilla.lower()]
        palabra_actual = semilla.lower()
        
        for _ in range(longitud - 1):
            # Buscamos todas las palabras posibles que pueden seguir a 'palabra_actual'
            candidatas = [w2 for (w1, w2) in self.frecuencias_bigramas.keys() if w1 == palabra_actual]
            
            if not candidatas:
                break # Llegamos a un callejón sin salida (una palabra que siempre estaba al final)
                
            # Extraemos las probabilidades de cada candidata
            probabilidades = [self.probabilidad(palabra_actual, cand) for cand in candidatas]
            
            # Elegimos la siguiente palabra ponderando por su probabilidad (Muestreo Aleatorio Ponderado)
            siguiente_palabra = random.choices(candidatas, weights=probabilidades, k=1)[0]
            texto_generado.append(siguiente_palabra)
            palabra_actual = siguiente_palabra
            
        return " ".join(texto_generado)

# --- EJEMPLO DE USO Y ANÁLISIS ---
print("--- Modelo Probabilístico de Lenguaje (Bigramas) ---\n")

# Modifiqué ligeramente el corpus para hacerlo más robusto y demostrar el muestreo aleatorio
texto_corpus = "el gato come pescado el gato duerme el perro corre rápido el perro come carne"
print(f"Corpus de entrenamiento: '{texto_corpus}'\n")

modelo = ModeloBigramas(texto_corpus)

print("1. Análisis de Probabilidades Exactas:")
print("   ¿Qué tan probable es que cierta palabra siga a la palabra 'el'?")
print(f"   - P(gato | el):   {modelo.probabilidad('el', 'gato'):.2f}  (Aparece 2 de 4 veces = 50%)")
print(f"   - P(perro | el):  {modelo.probabilidad('el', 'perro'):.2f}  (Aparece 2 de 4 veces = 50%)")
print(f"   - P(pájaro | el): {modelo.probabilidad('el', 'pájaro'):.2f}  (Aparece 0 de 4 veces = 0%)\n")

print("2. Generación de Texto Probabilístico (Decodificación):")
print(f"   Generando a partir de 'el': '{modelo.generar_texto('el', longitud=4)}'")
print(f"   Generando a partir de 'el': '{modelo.generar_texto('el', longitud=4)}'")