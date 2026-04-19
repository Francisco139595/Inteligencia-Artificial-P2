class CSP:
    """
    Define la estructura formal de un CSP: Variables, Dominios y Restricciones.
    Este es un ejemplo simple de coloreado de un mapa de 2 regiones.
    """
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones # Función que valida la consistencia

    def es_consistente(self, variable, valor, asignacion):
        """Verifica si asignar 'valor' a 'variable' viola alguna restricción."""
        for vecino in self.restricciones.get(variable, []):
            if vecino in asignacion and asignacion[vecino] == valor:
                return False
        return True

# Definición del problema
variables = ["Región A", "Región B"]
dominios = {v: ["Rojo", "Verde", "Azul"] for v in variables}
# Restricción: A y B deben tener colores diferentes
restricciones = {"Región A": ["Región B"], "Región B": ["Región A"]}

csp_ejemplo = CSP(variables, dominios, restricciones)
print("CSP de coloreado de mapa definido correctamente.")