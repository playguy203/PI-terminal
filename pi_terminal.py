import os
import time
import re

pi_str = ""


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

PI TERMINAL v4
""")


def barra_progreso():
    print("Cargando π...")
    for i in range(30):
        print("█", end="", flush=True)
        time.sleep(0.02)
    print("\n")


def cargar_pi_desde_txt():
    global pi_str

    barra_progreso()

    with open("pi.txt", "r") as f:
        pi_str = f.read().replace("\n", "").replace(".", "")

    print("Dígitos cargados:", len(pi_str))


def mostrar_contexto(pos, longitud):

    contexto = 20

    inicio = max(0, pos - contexto)
    fin = min(len(pi_str), pos + longitud + contexto)

    fragmento = pi_str[inicio:fin]

    print("\nContexto en π:\n")
    print("..." + fragmento + "...")

    flecha = " " * (pos - inicio + 3) + "↑"
    print(flecha)


def buscar_todas(secuencia):
    return [m.start() for m in re.finditer(secuencia, pi_str)]


def comando_search():

    numero = input("Número a buscar: ")

    resultados = buscar_todas(numero)

    if resultados:

        print("\nApariciones encontradas:", len(resultados))
        print("Primera aparición en posición:", resultados[0] + 1)

        mostrar_contexto(resultados[0], len(numero))

        if len(resultados) > 1:

            ver = input("\n¿Ver todas las posiciones? (s/n): ")

            if ver.lower() == "s":

                for r in resultados:
                    print(r + 1)

    else:
        print("No encontrado en los dígitos cargados")


def comando_pos():

    pos = int(input("Posición: "))

    if pos <= len(pi_str):

        print("Número en esa posición:", pi_str[pos-1])
        mostrar_contexto(pos-1, 1)

    else:
        print("Posición fuera del rango cargado")


def comando_pi():

    limpiar()
    print("π =\n")

    bloque = 5000

    for i in range(0, len(pi_str), bloque):
        print(pi_str[i:i+bloque])

    input("\nENTER para volver")


def comando_findme():

    numero = input("Ingresa tu número personal (ej. fecha): ")

    resultados = buscar_todas(numero)

    if resultados:

        print("\nTu número aparece en π")

        print("Total de apariciones:", len(resultados))
        print("Primera aparición en la posición:", resultados[0] + 1)

        mostrar_contexto(resultados[0], len(numero))

    else:
        print("\nTu número no aparece en los dígitos cargados")


def menu():

    while True:

        print("\nDígitos cargados:", len(pi_str))
        print("""
Comandos disponibles

search   buscar número en π
pos      ver número en una posición
pi       mostrar π completo
findme   buscar tu número personal
exit     salir
""")

        cmd = input("> ")

        if cmd == "search":
            comando_search()

        elif cmd == "pos":
            comando_pos()

        elif cmd == "pi":
            comando_pi()

        elif cmd == "findme":
            comando_findme()

        elif cmd == "exit":
            break

        else:
            print("Comando desconocido")


limpiar()
banner()
cargar_pi_desde_txt()
menu()
