def calcular_vpi(u_actual, u_con_info):
    """
    Calcula el Valor de la Información Perfecta (VPI).
    VPI = Utilidad esperada con información - Utilidad esperada sin ella.
    """
    vpi = u_con_info - u_actual
    return max(0, vpi)

# Supongamos que sin saber el clima mi mejor utilidad es 7.5
# Si supiera el clima antes de decidir, mi utilidad subiría a 9.2
u_sin = 7.5
u_con = 9.2

print(f"El precio máximo a pagar por la información es: {calcular_vpi(u_sin, u_con)}")