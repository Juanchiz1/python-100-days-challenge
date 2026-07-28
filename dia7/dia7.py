import random
import string

d_list=["Manzana","Papaya","Gato","Burro","Cafe","Plato","Silla","Amor","Dia","Noche","Lunes","Martes"]

#TODO-1 Randomly choose a word from the list

palabra=random.choice(d_list).upper()

longitud=len(palabra)

letras_adivinadas=set()

intentos_fallidos=0

palabra_actual = ["_"] * longitud

print("=============================")
print("     JUEGO DEL AHORCADO      ")
print(f"La palabra tiene {longitud} letras.")
print("=============================")


adivinar=''
vidas=6
errores=0
acierto=False
aciertos=0

# 2. Bucle del Juego
while vidas > 0:
    # Verificar si ya ha ganado el jugador (si no quedan guiones bajos)
    if "_" not in "".join(palabra_actual):
        print("\n🏆 ¡Felicidades! Has adivinado la palabra.")
        break  # Sale del bucle si ganó

    # 3. Input del Jugador (Manejo de Interacción)
    adivinar = input("Ingresa una letra: ").upper()

    if not adivinar.isalpha():
        print("❌ Por favor, ingresa solo una letra.")
        continue  # Vuelve al inicio del bucle sin penalizar vidas si no es una letra

    if adivinar in letras_adivinadas:
        print(f"⚠️ Ya intentaste la letra '{adivinar}'. Intenta con otra.")
        continue

    # Agregar la letra intentada para evitar repetirla y llevar un registro
    letras_adivinadas.add(adivinar)

    # 4. Lógica de Verificación
    encontrado = False
    for i in range(longitud):
        if palabra[i] == adivinar:
            palabra_actual[i] = adivinar
            encontrado = True
        elif palabra_actual[i] != adivinar:
            # Solo imprimimos si el espacio no ha sido llenado antes
            pass

    if encontrado:
        print("✅ ¡Buena letra! Has revelado algunas letras.")
    else:
        intentos_fallidos += 1
        vidas -= 1  # Perde una vida por cada intento fallido
        print(f"❌ No está en la palabra. Pierdes una vida.")

    # Mostrar el estado actual del juego (ej: _ A _ _ ...)
    print("\nEstado actual:", " ".join(palabra_actual))
    print(f"Vidas restantes: {vidas}")
    print(f"Letras usadas: {sorted(list(letras_adivinadas))}")

# 5. Fin del Juego (Post-Bucle)
print("\n=============================")

if vidas == 0:
    print("☠️ ¡Has perdido! No tienes más vidas.")
    print(f"La palabra era: {palabra}")
else:
    print("Juego completado (esto no debería pasar si el 'break' funciona).")








