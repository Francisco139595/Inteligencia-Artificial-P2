from typing import Dict, List

class ModeloPCFG:
    """
    Implementación demostrativa de una Gramática Probabilística Independiente del Contexto (PCFG).
    Asigna probabilidades a las reglas de producción para resolver ambigüedades sintácticas.
    """
    def __init__(self, reglas: Dict[str, float]):
        self.reglas = reglas

    def probabilidad_arbol(self, arbol_derivacion: List[str]) -> float:
        """
        Calcula la probabilidad conjunta de un árbol de derivación multiplicando
        las probabilidades de todas las reglas utilizadas para construirlo.
        """
        prob_total = 1.0
        for regla in arbol_derivacion:
            prob = self.reglas.get(regla, 0.0)
            if prob == 0.0:
                print(f" [!] Advertencia: La regla '{regla}' no existe en la gramática.")
            prob_total *= prob
        return prob_total

# --- EJEMPLO PRÁCTICO: RESOLUCIÓN DE AMBIGÜEDAD ---
def demostracion_pcfg():
    print("--- PCFG: Gramáticas Probabilísticas Independientes del Contexto ---\n")
    print("Problema: Ambigüedad Sintáctica en 'vi al hombre con el telescopio'.\n")
    
    # Definimos una gramática con probabilidades extraídas de un corpus (hipotético)
    gramatica = {
        "S -> VP": 1.0,
        # Opciones para el Sintagma Verbal (VP)
        "VP -> V NP": 0.6,
        "VP -> V NP PP": 0.4,  # Verbo modificado por preposición (Ej: usar telescopio para ver)
        # Opciones para el Sintagma Nominal (NP)
        "NP -> Det N": 0.7,
        "NP -> NP PP": 0.3,    # Sustantivo modificado por preposición (Ej: hombre que porta telescopio)
        "PP -> P NP": 1.0,
        # Reglas léxicas (palabras exactas con 100% prob para simplificar)
        "V -> vi": 1.0,
        "Det -> al": 1.0, "Det -> el": 1.0,
        "N -> hombre": 1.0, "N -> telescopio": 1.0,
        "P -> con": 1.0
    }
    
    modelo = ModeloPCFG(gramatica)
    
    # Árbol A: El Preposicional (PP) se adjunta al Verbo (VP)
    arbol_a = [
        "S -> VP", "VP -> V NP PP", "V -> vi", 
        "NP -> Det N", "Det -> al", "N -> hombre",
        "PP -> P NP", "P -> con", "NP -> Det N", "Det -> el", "N -> telescopio"
    ]
    
    # Árbol B: El Preposicional (PP) se adjunta al Sustantivo (NP)
    arbol_b = [
        "S -> VP", "VP -> V NP", "V -> vi", 
        "NP -> NP PP", "NP -> Det N", "Det -> al", "N -> hombre",
        "PP -> P NP", "P -> con", "NP -> Det N", "Det -> el", "N -> telescopio"
    ]
    
    prob_a = modelo.probabilidad_arbol(arbol_a)
    prob_b = modelo.probabilidad_arbol(arbol_b)
    
    print(f"Interpretación A (El telescopio es mi instrumento) -> Probabilidad: {prob_a:.5f}")
    print(f"Interpretación B (El hombre porta el telescopio)   -> Probabilidad: {prob_b:.5f}\n")
    print(f"-> El modelo elige la Interpretación {'A' if prob_a > prob_b else 'B'} por ser matemáticamente más probable.")

if __name__ == "__main__":
    demostracion_pcfg()
