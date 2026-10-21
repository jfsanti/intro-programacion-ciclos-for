"""
Se reciben N empleados, con 1 ≤ N ≤ 40. Cada registro contiene, en este orden,
identificador entero positivo único, edad entera no negativa en años y años enteros de
antigüedad entre 1 y 50. El sueldo ficticio es la suma de una base de 100 unidades monetarias,
el valor numérico de la edad y la suma de los enteros desde 1 hasta la antigüedad; toda esa
suma se divide entre los años de antigüedad. La edad y la suma de años se consideran aportes
numéricos en unidades monetarias dentro de este modelo ficticio. Informe el sueldo de cada

empleado, el total de la nómina y los identificadores con mayor y menor sueldo. En empate
conserve el primero recibido.

"""


N = int(input("Ingrese la cantidad de empleados: "))

if 1 <= N <= 40:
    total_nomina = 0
    mayor_sueldo = float('-inf')
    menor_sueldo = float('inf')
    identificador_mayor = None
    identificador_menor = None

    for empleados in range(1, N+1):
        identificador = int(input("Ingrese el identificador del empleado: "))
        edad = int(input("Ingrese la edad: "))
        antiguedad = int(input("Ingrese los años de antigüedad: "))

        if 1 <= antiguedad <= 50:
            suma_desde_1_hasta_antiguedad = sum(range(1, antiguedad + 1))
            sueldo = (100 + edad + suma_desde_1_hasta_antiguedad) / antiguedad
            total_nomina += sueldo

            if sueldo > mayor_sueldo:
                mayor_sueldo = sueldo
                identificador_mayor = identificador

            if sueldo < menor_sueldo:
                menor_sueldo = sueldo
                identificador_menor = identificador

            print("Sueldo del empleado ", identificador, ": ", sueldo)

    print("Total de la nómina: ", total_nomina)
    print("Identificador del empleado con mayor sueldo: ", identificador_mayor)
    print("Identificador del empleado con menor sueldo: ", identificador_menor)