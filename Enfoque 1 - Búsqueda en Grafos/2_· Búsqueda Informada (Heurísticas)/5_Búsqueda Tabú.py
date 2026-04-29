def tabu_search(max_iter=50, tam_lista=5):
    """
    Optimización que usa una memoria de corto plazo (Lista Tabú) 
    para evitar ciclos y salir de óptimos locales.
    """
    def fitness(x): return -(x**2) + 20
    
    actual = 10 # Estado inicial
    mejor_global = actual
    lista_tabu = [] # Aquí guardamos estados prohibidos
    
    for _ in range(max_iter):
        # Generamos vecinos (x+1, x-1)
        vecinos = [actual + 1, actual - 1]
        
        # Filtramos los que están en la lista tabú
        candidatos = [v for v in vecinos if v not in lista_tabu]
        
        if not candidatos: break
        
        # Elegimos el mejor del vecindario (aunque sea peor que el actual)
        actual = max(candidatos, key=fitness)
        
        # Actualizar lista tabú (FIFO)
        lista_tabu.append(actual)
        if len(lista_tabu) > tam_lista:
            lista_tabu.pop(0)
            
        # Guardar el mejor histórico
        if fitness(actual) > fitness(mejor_global):
            mejor_global = actual
            
    return mejor_global

print(f"Mejor valor con Búsqueda Tabú: {tabu_search()}")