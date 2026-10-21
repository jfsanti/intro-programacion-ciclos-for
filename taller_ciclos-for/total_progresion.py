"""
Ejercicio:
Se conoce el primer término A, la diferencia D y la cantidad N de términos de una
progresión. A y D son enteros entre -100 y 100, y N está entre 0 y 1000. Determine la suma de
los N términos; si N es cero, el total es cero.



"""

a = int(input("A? "))
d = int(input("D? "))
n = int(input("N? "))

if -100 <= a <= 100 and -100 <= d <= 100 and 0 <= n <= 1000:
    t = a
    suma = 0
    for k in range(n):
        suma = suma + t
        t = t + d

    print(suma)
else:
    print("Valores inválidos")