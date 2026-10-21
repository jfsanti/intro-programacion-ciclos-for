"""
Se reciben los tiempos de N ciclistas, con 1 ≤ N ≤ 20, sobre una vuelta de 250 metros.
Cada registro contiene identificador entero positivo único, minutos enteros no negativos,
segundos entre 0 y 59 y centésimas entre 0 y 99. Cada tiempo total es positivo. Informe la
velocidad media de cada ciclista en kilómetros por hora y el identificador del ganador. En
empate de tiempo gana el primero recibido.

"""

N = int(input("Ingrese la cantidad de ciclistas: "))

if 1 <= N <= 20:
    for ciclistas in range(1, N+1):
        identificador = int(input("Ingrese el identificador del ciclista: "))
        minutos = int(input("Ingrese los minutos: "))
        segundos = int(input("Ingrese los segundos: "))
        centesimas = int(input("Ingrese las centésimas: "))

        tiempo_total = (minutos * 60) + segundos + (centesimas / 100)
        velocidad_media = (0.25 / tiempo_total) * 3600

        print("Velocidad media del ciclista ", identificador, ": ", velocidad_media, " km/h")
        