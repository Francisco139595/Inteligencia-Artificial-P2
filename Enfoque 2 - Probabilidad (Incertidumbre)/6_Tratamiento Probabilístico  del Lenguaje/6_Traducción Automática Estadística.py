def traduccion_automatica_estadistica(frase_origen):
    """
    El modelo de Noisy Channel para traducción busca maximizar:
    P(E|F) ∝ P(F|E) * P(E)
    Donde P(F|E) es el modelo de traducción y P(E) es el modelo de lenguaje.
    """
    # Simplificación: Diccionario de probabilidades de traducción
    modelo_traduccion = {
        "the": "el",
        "cat": "gato",
        "eats": "come"
    }
    
    palabras = frase_origen.lower().split()
    traduccion = [modelo_traduccion.get(p, p) for p in palabras]
    
    return " ".join(traduccion)

frase = "The cat eats"
print(f"Traducción estadística (simplificada): {traduccion_automatica_estadistica(frase)}")