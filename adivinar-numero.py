import random

vidas = 3

numeros_aleatorios = random.randint(1, 10)

print("Intenta adivinar los numeros aleatorios del 1 al 10, solo tienes 3 vidas")

while vidas > 0:
    numero = input("Pon el numero del 1 al 10: ")

    if vidas == numeros_aleatorios:
        print("Bien hecho, haz adivinado el numero")
    else:
        vidas -= 1
        print(f"No le haz adivinado al numero, intentalo de nuevo. Vidas {vidas}")
        if vidas == 0:
            print("Haz perdido todas las vidas")
