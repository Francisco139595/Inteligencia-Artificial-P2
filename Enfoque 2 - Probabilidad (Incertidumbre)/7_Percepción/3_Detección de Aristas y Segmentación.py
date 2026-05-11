def detector_sobel_horizontal(pixeles):
    """
    Detección de bordes mediante el operador Sobel.
    Resalta los cambios bruscos de intensidad (gradientes).
    """
    # Máscara de Sobel horizontal (Kernel)
    # [[ -1, -2, -1 ],
    #  [  0,  0,  0 ],
    #  [  1,  2,  1 ]]
    gradiente = (pixeles[2][0] + 2*pixeles[2][1] + pixeles[2][2]) - \
                (pixeles[0][0] + 2*pixeles[0][1] + pixeles[0][2])
    return gradiente

# Supongamos una transición de negro (0) a blanco (255)
vecindad = [[0, 0, 0], [128, 128, 128], [255, 255, 255]]
print(f"Magnitud del borde detectado: {detector_sobel_horizontal(vecindad)}")