numero = int(input("Ingrese un número entero: "))  # Corregido Error 4: convertir a entero

if numero % 2 == 0:  # Corregido Error 1: usar '=='
    print("El número es par.")
else:
    print("El número es impar.")

cantidad = int(input("¿Cuántos números pares desea ver?: "))

contador = 0
i = 1

while contador < cantidad:  # Corregido Error 2: agregada ':'
    if i % 2 == 0:
        print("Par número", contador + 1, ":", i)  # Corregido Error 3: separar por comas
        contador += 1
    i += 1