def buscar_equilibrio_nash_puro(matriz_pagos):
    """
    Encuentra los Equilibrios de Nash en estrategias puras para un juego de 2 jugadores.
    La matriz debe ser: {(acción1, acción2): (pago1, pago2)}
    """
    equilibrios = []
    acciones_j1 = list(set(a[0] for a in matriz_pagos.keys()))
    acciones_j2 = list(set(a[1] for a in matriz_pagos.keys()))

    for a1 in acciones_j1:
        for a2 in acciones_j2:
            pago1, pago2 = matriz_pagos[(a1, a2)]
            
            # ¿Es a1 la mejor respuesta a a2?
            es_mejor_j1 = all(pago1 >= matriz_pagos[(alt, a2)][0] for alt in acciones_j1)
            # ¿Es a2 la mejor respuesta a a1?
            es_mejor_j2 = all(pago2 >= matriz_pagos[(a1, alt)][1] for alt in acciones_j2)
            
            if es_mejor_j1 and es_mejor_j2:
                equilibrios.append((a1, a2))
    return equilibrios

# El Dilema del Prisionero
juego = {
    ("Callar", "Callar"): (-1, -1),
    ("Callar", "Delatar"): (-3, 0),
    ("Delatar", "Callar"): (0, -3),
    ("Delatar", "Delatar"): (-2, -2)
}

print(f"Equilibrio de Nash (Estrategia Pura): {buscar_equilibrio_nash_puro(juego)}")