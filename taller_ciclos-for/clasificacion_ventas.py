"""
Un vendedor tiene N ventas, con 0 ≤ N ≤ 1000, y se recibe el importe no negativo de cada
una. Informe cuántas fueron de 200 o menos, cuántas superaron 200 sin llegar a 400 y cuántas
fueron de 400 o más. Una venta pertenece a un solo grupo.

"""

N = int(input("Ingrese la cantidad de ventas: "))

if 0 <= N <= 1000:
    for ventas in range(1, N+1):
        ventas = float(input("Ingrese el importe de la venta: "))
elif 200 < ventas:
    grupo = print("1")
elif 200 <= ventas < 400:
    grupo = print("2")
elif ventas >= 400:
    grupo = print("3")

print("Pertenece a: ", 200 < ventas, 200 <= ventas < 400, ventas >= 400)



