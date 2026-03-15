import os
import time

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

PI TERMINAL v3
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


def comando_search():

    numero = input("Número a buscar: ")

    pos = pi_str.find(numero)

    if pos != -1:
        print("Encontrado en posición:", pos + 1)
        mostrar_contexto(pos, len(numero))
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


def comando_load():
    print("π ya está cargado desde el archivo pi.txt")


def comando_findme():

    numero = input("Ingresa tu número personal (ej. fecha): ")

    pos = pi_str.find(numero)

    if pos != -1:
        print("Tu número aparece en π en la posición:", pos + 1)
        mostrar_contexto(pos, len(numero))
    else:
        print("Tu número no aparece en los dígitos cargados")


def menu():

    while True:

        print("\nDígitos cargados:", len(pi_str))
        print("""
Comandos disponibles

search   buscar número en π
pos      ver número en una posición
pi       mostrar π completo
load     informar sobre carga de π
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

        elif cmd == "load":
            comando_load()

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