bandas = []

opcion = 100
while (opcion != 5):
    print ("*** FESTIVAL ALTAVOZ ***")
    print ("************************")
    print ("1 - REGISTRAR BANDA")
    print ("2 - VER EL CARTEL DEL FESTIVAL")
    print ("3 - BUSCAR BANDA")
    print ("4 - MODIFICAR BANDA")
    print ("5 - FINALIZAR")
    opcion = int (input("Digita una opcion: "))

    if opcion == 1:
        banda = {}
        # se llena el objeto de banda
        banda ["ID"]= int(input("Digite el ID: "))
        banda ["Nombre"]= input("Digita el Nombre: ")
        banda ["Genero"]= input("Digita el Género: ")
        banda ["Clasificacion"]= int(input("Digita la Clasificacion: "))
        banda ["Costo"]= int(input("Digita el Costo: "))
        banda ["Tiempo"]= int(input("Digita el Tiempo: "))

        # como agrego un diccionario a una lista
        bandas.append(banda)
                
    elif opcion == 2:
        # recorriendo una lista para imprimir sus elementos
        for bandaAuxiliar in bandas:
            print(f"{bandaAuxiliar["ID"]}--{bandaAuxiliar["Nombre"]}")

    elif opcion == 3:
        # buscando un elemento dentro de una lista
        bandaBuscada = input ("Digita la banda que quieres buscar: ")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar ["Nombre"] == bandaBuscada
                print("se encontró el valor")
            else:
                print("No se encontró el valor")

    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else: 
        print ("Opcion inválida")
