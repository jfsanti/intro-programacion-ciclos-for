"""
Una empresa tiene N empleados, con 0 ≤ N ≤ 1000. Se recibe el sueldo no negativo de
cada empleado y se desea el total de la nómina. Para una empresa sin empleados, el total es
cero.


"""

n_empleados = int(input("Ingrese la cantidad de empleados: "))
suma = 0.0
if 0 <= n_empleados <= 1000:
    for veces in range(1, n_empleados + 1):
        print("Empleado #", veces)
        sueldo = float(input("\nSueldos: "))
        suma = suma + sueldo
else:
    print("No valido")
print("La nómina es: ", suma)


