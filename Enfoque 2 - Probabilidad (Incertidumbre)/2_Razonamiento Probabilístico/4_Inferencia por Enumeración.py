from typing import Any

def inferencia_por_enumeracion(variable_consulta: str, evidencia: dict, red: Any) -> str:
    """
    Calcula P(X | e) sumando sobre todas las variables ocultas.
    Es un método exacto pero de complejidad exponencial.
    """
    # En un entorno real, este algoritmo recursivo recorre el árbol de variables.
    # Aquí simplificamos el concepto de 'Sumar sobre variables ocultas (Y)'.
    print(f"Inferencia: Evaluando todas las combinaciones de variables ocultas para {variable_consulta}.")
    return "Resultado normalizado de la suma de probabilidades conjuntas."

# Clase genérica para evitar un NameError al probar la función
class RedSimulada:
    pass

red = RedSimulada()

print(inferencia_por_enumeracion("Alarma", {"Robo": True}, red))