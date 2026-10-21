"""
Ejercicio:
Una pantalla debe presentar todos los enteros comprendidos entre dos límites A y B,
ambos incluidos, empezando por A y terminando en B. Los límites son enteros entre -100 y
100. Si coinciden, presente ese único valor.

ENTRADA
- A_limite: ingrese el numero entero
- B_limite: ingrese le numero entero

PROCESO



SALIDA



"""

A_limite = int((input("Ingrese el límite en A: ")))
B_limite = int((input("Ingrese el límite en B: ")))

if -100 <= A_limite <= 100 and -100 <= B_limite <= 100:
    if A_limite < B_limite: 
        for num in range(A_limite, B_limite + 1):
            print(num)

    elif A_limite == B_limite:
        print(A_limite)

    else:
        for num in range(A_limite, B_limite - 1, -1):
            print(num)
else:
    print("Error: limites invalídos")
