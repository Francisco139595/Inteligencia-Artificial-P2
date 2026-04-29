def calcular_probabilidad_conjunta(factores):
    """
    La Regla de la Cadena permite calcular la probabilidad conjunta de 
    múltiples variables: P(X1, ..., Xn) = Π P(Xi | Padres(Xi)).
    """
    prob_total = 1.0
    for prob_condicional in factores:
        prob_total *= prob_condicional
    return prob_total

# Ejemplo: P(Nublado, Lluvia, HierbaMojada)
# P(N) * P(L|N) * P(H|L)
p_n = 0.9
p_l_dado_n = 0.4
p_h_dado_l = 0.2

conjunta = calcular_probabilidad_conjunta([p_n, p_l_dado_n, p_h_dado_l])
print(f"P(Nublado, Lluvia, HierbaMojada) = {conjunta:.3f}")