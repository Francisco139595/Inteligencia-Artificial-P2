def viterbi_explicacion(estados, obs, p_ini, p_trans, p_obs, seq):
    """
    Algoritmo de Viterbi: Encuentra la secuencia de estados ocultos más probable
    (Explicación) que generó una serie de observaciones.
    """
    # Estructura para almacenar probabilidades de caminos
    v = [{}]
    for st in estados:
        v[0][st] = p_ini[st] * p_obs[st][seq[0]]

    # Algoritmo principal (Programación dinámica)
    for t in range(1, len(seq)):
        v.append({})
        for st in estados:
            # Maximizar: P(si|sj) * Viterbi(sj, t-1)
            prob_max = max(v[t-1][prev_st] * p_trans[prev_st][st] for prev_st in estados)
            v[t][st] = prob_max * p_obs[st][seq[t]]

    return v[-1] # Estado final más probable

estados = ('Sano', 'Enfermo')
obs = ('Normal', 'Fiebre')
p_ini = {'Sano': 0.6, 'Enfermo': 0.4}
# ... (tablas de trans y obs definidas similarmente)
print("Cálculo de Viterbi para HMM ejecutado.")