def verificar_independencia_condicional(p_a_dado_bc, p_a_dado_c):
    """
    A y B son independientes condicionalmente dado C si:
    P(A | B, C) = P(A | C)
    Esto significa que si ya conocemos C, saber B no aporta nueva información sobre A.
    """
    # Tolerancia para comparaciones de punto flotante
    es_independiente = abs(p_a_dado_bc - p_a_dado_c) < 1e-6
    return es_independiente

# Ejemplo: A=Alarma, B=JuanLlamó, C=Robo
# Si sabemos que hubo un Robo(C), ¿saber que Juan llamó(B) cambia la prob de Alarma(A)?
print(f"¿Es independiente?: {verificar_independencia_condicional(0.9, 0.9)}")