import string
from typing import List, Tuple, Dict

def extraccion_entidades_relaciones(texto: str, base_conocimiento: Dict[str, str]) -> dict:
    """
    La extracción de información identifica entidades (Nombres, Lugares) 
    y relaciones lógicas en texto no estructurado.
    """
    # 1. Limpieza de puntuación para evitar fallos con comas o puntos (ej. "México,")
    texto_limpio = texto.translate(str.maketrans('', '', string.punctuation))
    palabras = texto_limpio.split()
    
    # Convertimos la base de conocimiento a minúsculas para búsquedas insensibles a mayúsculas
    conocimiento_lower = {k.lower(): v for k, v in base_conocimiento.items()}
    
    entidades_encontradas = []
    tipos_presentes = set()
    
    # 2. Extracción de Entidades (NER - Named Entity Recognition)
    for palabra in palabras:
        palabra_lower = palabra.lower()
        if palabra_lower in conocimiento_lower:
            tipo = conocimiento_lower[palabra_lower]
            entidades_encontradas.append((palabra, tipo))
            tipos_presentes.add(tipo)
            
    # 3. Extracción de Relaciones (Basada en heurísticas de co-ocurrencia)
    relaciones = []
    if "ORGANIZACIÓN" in tipos_presentes and "LUGAR" in tipos_presentes:
        relaciones.append("Sede_Ubicada_En(Sujeto: ORGANIZACIÓN, Objeto: LUGAR)")
    if "ORGANIZACIÓN" in tipos_presentes and "TECNOLOGÍA" in tipos_presentes:
        relaciones.append("Utiliza(Sujeto: ORGANIZACIÓN, Objeto: TECNOLOGÍA)")
        
    return {"entidades": entidades_encontradas, "relaciones": relaciones}

# --- EJEMPLO DE USO Y ANÁLISIS ---
conocimiento = {
    "Google": "ORGANIZACIÓN",
    "México": "LUGAR",
    "Arduino": "TECNOLOGÍA"
}

# Nota cómo ahora soporta comas y variaciones en mayúsculas ("arduino")
texto_input = "Google tiene oficinas en México, y usa tecnología arduino."
resultados = extraccion_entidades_relaciones(texto_input, conocimiento)

print("--- Sistema de Extracción de Información ---")
print(f"Texto original: '{texto_input}'\n")
print(f"1. Entidades Detectadas (NER):\n   {resultados['entidades']}\n")
print(f"2. Relaciones Lógicas Inferidas:\n   {resultados['relaciones']}")