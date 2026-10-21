"""
Ejemplo:
Calcular el factorial de un numero.

fact(n): 1 x 2 x 3 .. x n; 0! = 1

ejemplo:
5! = 1 x 2 x 3 x 4 x 5 = 120 

- pass : sirve para que no haga nada y deje pasar al siguiente
"""

n = int(input("n? "))

if n == 0:
    print(1)
elif n > 0:
    fact = 1
    for num in range(1, n+1):
        fact = fact * num
    print(n, "!=", fact) # no se pone dentro del for porque si no se va a repetir cada vez, se pone afuera para q solo imprima al final
else:
    print("Error. n deber mayor o igual a cero. ")