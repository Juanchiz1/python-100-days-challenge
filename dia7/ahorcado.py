import random


d_list = ["Manzana", "Papaya", "Gato", "Burro", "Cafe", "Plato", "Silla", "Amor", "Dia", "Noche", "Lunes", "Martes"]

# TODO-1 Randomly choose a word from the list
palabra = random.choice(d_list).upper()

longitud = len(palabra)

letras_encontradas=set()

palabra_actual=[]

print(palabra)
# print(longitud) # Mejor no mostrarlo, es mejor que el usuario solo vea los guiones bajos.

palabra_actual=["_"]*longitud

adivinar = ''

vidas = 6
errores = 0
encontrado = False

while vidas > 0:
    if "_" not in "".join(palabra_actual):
        print("\n🏆 ¡Felicidades! Has adivinado la palabra.")
        break  # Sale del bucle si ganó

    adivinar = input("Ingresa una letra de la palabra \n").upper()
    if adivinar in letras_encontradas:
        print("Ya Adivinaste esta Letra")
    letras_encontradas.add(adivinar)

    for i in range(longitud):
        if palabra[i] == adivinar:
            palabra_actual[i] = adivinar
            encontrado = True
        elif palabra_actual[i] != adivinar:
            pass

        if encontrado:
            print("✅ ¡Buena letra! Has revelado algunas letras.")
        else:
            errores += 1
            vidas -= 1  # Perde una vida por cada intento fallido
            print(f"❌ No está en la palabra. Pierdes una vida.")

            # Mostrar el estado actual del juego (ej: _ A _ _ ...)
        print("\nEstado actual:", " ".join(palabra_actual))
        print(f"Vidas restantes: {vidas}")
        print(f"Letras usadas: {sorted(list(letras_encontradas))}")

    # 5. Fin del Juego (Post-Bucle)
print("\n=============================")

if vidas == 0:
    print("☠️ ¡Has perdido! No tienes más vidas.")
    print(f"La palabra era: {palabra}")
else:
    print("Juego completado.")

