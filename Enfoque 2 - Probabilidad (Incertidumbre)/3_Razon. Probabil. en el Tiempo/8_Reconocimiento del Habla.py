from typing import Dict

def reconocimiento_habla_modelo(audio_observado: str, modelo_acustico: Dict[str, float], modelo_lenguaje: Dict[str, float]) -> str:
    """
    El reconocimiento del habla combina un modelo acústico (HMM/Redes Neuronales)
    y un modelo de lenguaje (N-gramas/Transformers).
    
    Teorema de Bayes aplicado al reconocimiento de voz:
    P(Palabra | Audio) ∝ P(Audio | Palabra) * P(Palabra)
    """
    print(f"--- Sistema de Reconocimiento del Habla ---")
    print(f"Audio capturado (fonemas aproximados): '{audio_observado}'\n")
    
    # 1. Modelo Acústico: P(Audio | Palabra)
    # -> ¿Qué tan probable es que esta palabra genere los sonidos (fonemas) que acabamos de escuchar?
    print("1. Modelo Acústico: Evaluando coincidencia fonética...")
    
    # 2. Modelo de Lenguaje: P(Palabra)
    # -> ¿Qué tan común es esta palabra en el idioma o contexto actual?
    print("2. Modelo de Lenguaje: Evaluando probabilidad previa de la palabra...\n")
    
    # 3. Decodificación (Búsqueda de la hipótesis más probable combinando ambas probabilidades)
    mejor_palabra = ""
    max_probabilidad = -1.0
    
    print("3. Decodificación (argmax P(Audio | Palabra) * P(Palabra)):")
    for palabra in modelo_lenguaje.keys():
        p_audio_dado_palabra = modelo_acustico.get(palabra, 0.01)
        p_palabra = modelo_lenguaje.get(palabra, 0.01)
        
        # Calcular probabilidad conjunta (proporcional a la probabilidad a posteriori)
        prob_conjunta = p_audio_dado_palabra * p_palabra
        
        print(f"   -> Hipótesis '{palabra}': {p_audio_dado_palabra:.2f} (Acústico) * {p_palabra:.2f} (Lenguaje) = {prob_conjunta:.4f}")
        
        if prob_conjunta > max_probabilidad:
            max_probabilidad = prob_conjunta
            mejor_palabra = palabra
            
    print(f"\nResultado final: La palabra más probable es '{mejor_palabra}'.")
    return mejor_palabra

# --- Simulación ---
# El usuario dijo algo que el micrófono captó como "ola"
sim_modelo_acustico = {"hola": 0.95, "ola": 0.90, "ala": 0.30}
sim_modelo_lenguaje = {"hola": 0.80, "ola": 0.15, "ala": 0.05}

reconocimiento_habla_modelo("ola", sim_modelo_acustico, sim_modelo_lenguaje)