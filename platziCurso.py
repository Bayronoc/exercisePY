#Selecciona tus numeros del 1 al 10:
import random as rn

# Seleccionar 2 números válidos
numeros_elegidos = []
for i in range(2):
    numero = int(input("Elige un numero del 1 al 10: "))
    while not (1 <= numero <= 10):   # validación con booleano
        print("Numero invalido. Intenta de nuevo.")
        numero = int(input("Elige un numero del 1 al 10: "))
    numeros_elegidos.append(numero)

print("Tus numeros elegidos son:", numeros_elegidos)

# Generar número aleatorio del 1 al 10
numero_ganador = rn.randint(1, 10)

# Validación usando expresión booleana
ganaste = numero_ganador in numeros_elegidos   # <--- booleano clave

if ganaste:
    print(f"¡Felicidades! Has ganado. El número ganador era {numero_ganador}")
else:
    print(f"Lo siento, has perdido. El número ganador era {numero_ganador}")