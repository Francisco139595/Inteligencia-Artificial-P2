from typing import List, Dict, Any

def eliminacion_variables(consulta: str, evidencia: Dict[str, Any], variables_ocultas: List[str], factores: List[str]) -> str:
    """
    Optimización de la enumeración que usa programación dinámica para 
    almacenar cálculos intermedios (factores) y evitar cálculos repetidos.
    """
    print(f"--- Iniciando Eliminación de Variables ---")
    print(f"Consulta: P({consulta} | {evidencia})")
    
    # Paso 1: Restringir factores usando la evidencia
    print("Paso 1: Reduciendo los factores basándose en la evidencia observada.")
    
    # Paso 2: Eliminar las variables ocultas secuencialmente
    for var in variables_ocultas:
        print(f"\nPaso 2: Eliminando variable oculta '{var}'...")
        print(f"  -> Agrupando y multiplicando factores que contienen a '{var}'.")
        print(f"  -> Sumando (marginando) la variable '{var}' para crear un nuevo factor.")
        
    # Paso 3: Producto final y normalización
    print(f"\nPaso 3: Multiplicando factores restantes y normalizando el resultado final para '{consulta}'.")
    
    return f"-> Resultado: Distribución probabilística calculada para '{consulta}'."

# Simulación de los parámetros de entrada del algoritmo
factores_iniciales = ["P(Robo)", "P(Terremoto)", "P(Alarma|Robo,Terremoto)", "P(JuanLlama|Alarma)"]
resultado = eliminacion_variables(consulta="Robo", evidencia={"JuanLlama": True}, variables_ocultas=["Terremoto", "Alarma"], factores=factores_iniciales)
print(f"\n{resultado}")