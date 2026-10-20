comentarios = []

def registrar_comentario():
    texto = input("Escriba el comentario: ").strip()
    if texto != "":
        comentarios.append(texto)
        print("Comentario registrado.")
    else:
        print("El comentario no puede estar vacio.")

def mostrar_comentarios():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
    else:
        for i in range(len(comentarios)):
            print(i + 1, comentarios[i])

def buscar_palabra():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return
    p = input("Ingrese la palabra a buscar: ").strip().lower()
    encontrado = False
    for i in range(len(comentarios)):
        if p in comentarios[i].lower():
            print(f"{i + 1}. {comentarios[i]}")
            encontrado = True
    if not encontrado:
        print("No se encontraron coincidencias.")

def contar_palabras():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
    else:
        for i in range(len(comentarios)):
            cant = len(comentarios[i].split())
            print(f"Comentario {i + 1}: {cant} palabras")

def contar_apariciones():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return
    mostrar_comentarios()
    try:
        idx = int(input("Seleccione el numero del comentario: ")) - 1
        if idx < 0 or idx >= len(comentarios):
            print("Numero invalido.")
            return
        com = comentarios[idx]
        pal = input("Ingrese la palabra a contar: ").strip().lower()
        res = com.lower().count(pal)
        print(f"La palabra aparece {res} veces.")
    except ValueError:
        print("Debe ingresar un numero valido.")

def resumen_tupla():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return
    mostrar_comentarios()
    try:
        idx = int(input("Seleccione el numero del comentario: ")) - 1
        if idx < 0 or idx >= len(comentarios):
            print("Numero invalido.")
            return
        com = comentarios[idx]
        pal = input("Ingrese la palabra para el resumen: ").strip().lower()
        c_char = len(com)
        c_pal = len(com.split())
        c_ap = com.lower().count(pal)
        resumen = (c_char, c_pal, c_ap)
        print("\n--- RESUMEN ---")
        print("Caracteres:", resumen[0])
        print("Palabras:", resumen[1])
        print("Apariciones de la palabra:", resumen[2])
    except ValueError:
        print("Debe ingresar un numero valido.")

def menu():
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Registrar un comentario")
        print("2. Mostrar todos los comentarios")
        print("3. Buscar comentarios por palabra")
        print("4. Mostrar la cantidad de palabras de cada comentario")
        print("5. Contar apariciones de una palabra")
        print("6. Mostrar resumen en tupla")
        print("7. Salir")
        op = input("Seleccione una opcion: ").strip()
        if op == "1":
            registrar_comentario()
        elif op == "2":
            mostrar_comentarios()
        elif op == "3":
            buscar_palabra()
        elif op == "4":
            contar_palabras()
        elif op == "5":
            contar_apariciones()
        elif op == "6":
            resumen_tupla()
        elif op == "7":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    menu()