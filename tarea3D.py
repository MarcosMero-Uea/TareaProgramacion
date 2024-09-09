# Matriz de temperaturas para 3 ciudades, 2 semanas, 7 días
temperaturas = [
    [
        [20, 21, 22, 23, 24, 25, 26],  # Ciudad 1 - Semana 1
        [25, 24, 23, 22, 21, 20, 19]   # Ciudad 1 - Semana 2
    ],
    [
        [15, 16, 17, 18, 19, 20, 21],  # Ciudad 2 - Semana 1
        [20, 21, 22, 23, 24, 25, 26]   # Ciudad 2 - Semana 2
    ],
    [
        [30, 31, 32, 33, 34, 35, 36],  # Ciudad 3 - Semana 1
        [35, 34, 33, 32, 31, 30, 29]   # Ciudad 3 - Semana 2
    ]
]

# Calcular y mostrar los promedios
for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad {i+1}:")
    for j, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)
        print(f"  Promedio de semana {j+1}: {promedio:.2f}")
