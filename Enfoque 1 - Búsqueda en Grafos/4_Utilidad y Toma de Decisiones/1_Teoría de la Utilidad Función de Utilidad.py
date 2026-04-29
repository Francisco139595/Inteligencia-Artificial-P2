import math

def funcion_utilidad_esperada(opciones, probabilidades):
    """
    Calcula la utilidad esperada de diferentes decisiones bajo riesgo.
    Usa una función de utilidad logarítmica para modelar la aversión al riesgo.
    """
    def utilidad(moneda):
        # La utilidad suele ser logarítmica (ganar $100 no es el doble de feliz que $50)
        return math.log(moneda) if moneda > 0 else 0

    resultados = {}
    for nombre, pagos in opciones.items():
        # U(E) = sum( P(i) * U(pago_i) )
        u_esperada = sum(probabilidades[i] * utilidad(pagos[i]) for i in range(len(pagos)))
        resultados[nombre] = u_esperada

    return resultados

# Ejemplo: Elegir entre un pago seguro o una apuesta
opciones = {
    "Seguro": [50, 50],
    "Apuesta": [0, 150]
}
probs = [0.5, 0.5]

print("Utilidades esperadas:", funcion_utilidad_esperada(opciones, probs))