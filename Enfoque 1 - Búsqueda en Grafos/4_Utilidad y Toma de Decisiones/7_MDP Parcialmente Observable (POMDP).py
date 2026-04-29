def pomdp_creencia(creencia_actual, accion, observacion, P_trans, P_obs):
    """
    Actualiza el 'Belief State' (estado de creencia) en un POMDP.
    b'(s') = alpha * P(o|s') * sum( P(s'|s,a) * b(s) )
    """
    nueva_creencia = {}
    for s_sig in P_trans:
        prob_trans = sum(creencia_actual[s] * P_trans[s][accion].get(s_sig, 0) for s in creencia_actual)
        nueva_creencia[s_sig] = P_obs[s_sig].get(observacion, 0) * prob_trans

    # Normalización (alpha)
    total = sum(nueva_creencia.values())
    return {s: v / total for s, v in nueva_creencia.items()}

# Ejemplo: Creencia sobre si hay un tesoro (T) o no (N)
b = {"T": 0.5, "N": 0.5}
print("Nueva creencia tras observar:", pomdp_creencia(b, "esperar", "ruido", {"T": {"esperar": {"T": 1.0}}, "N": {"esperar": {"N": 1.0}}}, {"T": {"ruido": 0.8}, "N": {"ruido": 0.2}}))