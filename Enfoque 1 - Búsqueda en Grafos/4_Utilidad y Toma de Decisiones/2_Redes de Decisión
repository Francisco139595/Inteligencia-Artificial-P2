def red_decision_simple(clima_prob, utilidad_paraguas):
    """
    Representa una red de decisión básica con un nodo de azar (clima),
    un nodo de decisión (llevar paraguas) y un nodo de utilidad.
    """
    # Probabilidades: Sol 0.7, Lluvia 0.3
    # Utilidades: {Decisión: {Estado: Valor}}
    
    decisiones = ["Llevar", "No Llevar"]
    mejores_opciones = {}

    for d in decisiones:
        u_lluvia = clima_prob['Lluvia'] * utilidad_paraguas[d]['Lluvia']
        u_sol = clima_prob['Sol'] * utilidad_paraguas[d]['Sol']
        mejores_opciones[d] = u_lluvia + u_sol

    return max(mejores_opciones, key=mejores_opciones.get)

prob_clima = {'Sol': 0.7, 'Lluvia': 0.3}
utilidades = {
    "Llevar": {"Sol": 2, "Lluvia": 10},
    "No Llevar": {"Sol": 10, "Lluvia": 0}
}

print(f"Mejor decisión en la red: {red_decision_simple(prob_clima, utilidades)}")
