"""
Ejemplo:
Un profesor necesita crear un programa que le ayude a clacular el promedio de natoas de un salon de clases.
El ingresa el nombre y el valor de nota final de cada estudiante.
Al final necesita saber cual es el mejor estudiante y el promedio de todo el curso.
Cada nota es de 0 a 5.0
"""

cantidad_est = int(input("Cantidad de estudiantes? "))

mejor_est = ""
nota_mayor = 0.0
suma = 0.0
promedio = 0.0

for veces in range(1, cantidad_est+1): 
    print("Estudiante #", veces)
    nombre = input("Nombre del estudiante: ")
    nota = float(input("Nota del estudiante: "))

    suma = suma + nota #<- Acumuladores

    if nota  > nota_mayor:  #Encontrar el estudiante con mayor nota
        nota_mayor = nota
        mejor_est = nombre

promedio = suma / cantidad_est

print("El promedio del curso es:", promedio)
print("El mejor estudiante es: ", mejor_est, "con nota de:", nota_mayor)