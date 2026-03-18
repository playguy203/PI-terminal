import os
import time
import re
import random
from collections import Counter

pi_str = ""
errores = 0


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print("""
██████╗ ██╗    ████████╗███████╗██████╗ ███╗   ███╗
██╔══██╗██║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
██████╔╝██║       ██║   █████╗  ██████╔╝██╔████╔██║
██╔═══╝ ██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║
██║     ██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
╚═╝     ╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝

PI TERMINAL v7
""")


def barra_progreso():
    print("Cargando π...")
    for _ in range(30):
        print("█", end="", flush=True)
        time.sleep(0.02)
    print("\n")


def cargar_pi_desde_txt():
    global pi_str

    barra_progreso()

    with open("pi.txt", "r") as f:
        pi_str = f.read().replace("\n", "").replace(".", "")

    print("Dígitos cargados:", len(pi_str))


# =========================
# CONTEXTO CON RESALTADO
# =========================

def mostrar_contexto(pos, longitud):

    contexto = 20
    inicio = max(0, pos - contexto)
    fin = min(len(pi_str), pos + longitud + contexto)

    fragmento = pi_str[inicio:fin]

    resaltado = (
        fragmento[:pos - inicio] +
        "[" + fragmento[pos - inicio:pos - inicio + longitud] + "]" +
        fragmento[pos - inicio + longitud:]
    )

    print("\nContexto en π:\n")
    print("..." + resaltado + "...")


# =========================
# EASTER EGGS
# =========================

def easter_egg(numero):

    if numero == "666":
        print("\n⚠️ Has invocado algo que no debías...")
    elif numero == "42":
        print("\nRespuesta al sentido de la vida detectada.")
    elif numero == "314":
        print("\nMuy gracioso... estás buscando π dentro de π.")
    elif numero == "777":
        print("\nSuerte máxima detectada 🍀")
    elif numero == "123456":
        print("\nSecuencia sospechosamente ordenada...")
    elif numero == "000":
        print("\nEl vacío absoluto.")
    elif numero == "73":
        print("\nSheldon tenía razón.")


# =========================
# BÚSQUEDA
# =========================

def buscar_todas(secuencia):
    return [m.start() for m in re.finditer(re.escape(secuencia), pi_str)]


def buscar_patron(patron):
    try:
        return [(m.start(), len(m.group())) for m in re.finditer(patron, pi_str)]
    except re.error:
        print("Patrón inválido")
        return []


def comando_search():

    numero = input("Número a buscar: ")
    easter_egg(numero)

    resultados = buscar_todas(numero)

    if resultados:

        print("\nApariciones:", len(resultados))
        print("Primera posición:", resultados[0] + 1)

        mostrar_contexto(resultados[0], len(numero))

    else:
        print("No encontrado")


def comando_pattern():

    print("\nModo regex")
    patron = input("Patrón: ")

    resultados = buscar_patron(patron)

    if resultados:
        pos, longitud = resultados[0]

        print("\nApariciones:", len(resultados))
        print("Primera posición:", pos + 1)

        mostrar_contexto(pos, longitud)

    else:
        print("No encontrado")


# =========================
# POSICIÓN
# =========================

def comando_pos():

    try:
        pos = int(input("Posición: "))
    except:
        print("Entrada inválida")
        return

    if pos <= len(pi_str):

        print("Número:", pi_str[pos - 1])

        if pos == 1:
            print("El inicio de todo.")
        elif pos == 314:
            print("Referencia directa a π.")
        elif pos == 666:
            print("...esa posición está maldita.")

        mostrar_contexto(pos - 1, 1)

    else:
        print("Fuera de rango")


# =========================
# π (TROLL)
# =========================

def comando_pi():
    print("\nCargando π completo...")
    time.sleep(1)
    print("Error: π es demasiado largo para tu mente.")
    input("\nENTER para volver")


# =========================
# RAREZA
# =========================

def comando_findme():

    numero = input("Tu número: ")
    easter_egg(numero)

    resultados = buscar_todas(numero)

    if resultados:

        total = len(resultados)
        densidad = len(pi_str) / total

        print("\nApariciones:", total)
        print("Primera:", resultados[0] + 1)
        print(f"Frecuencia: 1 cada {int(densidad)} dígitos")

        if densidad < 50:
            print("Nivel: ULTRA COMÚN")
        elif densidad < 200:
            print("Nivel: COMÚN")
        elif densidad < 1000:
            print("Nivel: RARO")
        else:
            print("Nivel: EXTREMADAMENTE RARO")

        mostrar_contexto(resultados[0], len(numero))

    else:
        print("No aparece")


# =========================
# ESTADÍSTICAS
# =========================

def comando_stats():

    conteo = Counter(pi_str)
    total = len(pi_str)

    print("\nDistribución:\n")

    for d in sorted(conteo.keys()):
        cantidad = conteo[d]
        porcentaje = (cantidad / total) * 100
        barra = "█" * int(porcentaje * 2)

        print(f"{d}: {cantidad} ({porcentaje:.2f}%) {barra}")


# =========================
# 🎮 MODO JUEGO
# =========================

def comando_game():

    print("\nModo juego: adivina los siguientes 3 dígitos")

    pos = random.randint(1, len(pi_str) - 4)
    real = pi_str[pos:pos + 3]

    print("Posición:", pos)

    intento = input("Tu respuesta: ")

    if intento == real:
        print("✔ Correcto")
    else:
        print("✘ Incorrecto. Era:", real)


# =========================
# MENÚ
# =========================

def menu():
    global errores

    while True:

        print("\nDígitos:", len(pi_str))
        print("""
search   buscar
pattern  regex
pos      posición
pi       π completo
findme   tu número
stats    estadísticas
game     jugar
exit     salir
""")

        cmd = input("> ")

        if cmd == "search":
            comando_search()

        elif cmd == "pattern":
            comando_pattern()

        elif cmd == "pos":
            comando_pos()

        elif cmd == "pi":
            comando_pi()

        elif cmd == "findme":
            comando_findme()

        elif cmd == "stats":
            comando_stats()

        elif cmd == "game":
            comando_game()

        elif cmd == "whoami":
            print("Explorador de π")

        elif cmd == "xyzzy":
            print("Nada sucede.")

        elif cmd == "exit":
            break

        else:
            errores += 1

            if errores == 3:
                print("¿Seguro?")
            elif errores == 5:
                print("Lee el menú")
            elif errores == 10:
                print("Ya es preocupante")
            else:
                print("Comando desconocido")


# =========================
# MAIN
# =========================

limpiar()
banner()
cargar_pi_desde_txt()
menu()
