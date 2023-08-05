nombre = input("Nombre del empleado: ")
ingreso = float(input("ingreso del usuario: "))

comision = (ingreso * 13) / 100

print(f"El empleado {nombre} ha tenido unos ingresos totales de {round(comision,2)}")
