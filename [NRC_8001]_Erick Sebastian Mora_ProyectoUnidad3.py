import time
import os

def validarNumeros():
    """
    Es un procedimiento generico alternativo para realizar validacion de numeros enteros
    del 0 al 20 los datos ingresados se leen como string (str) y si son numeros se verifican
    y se transforman en tipo de datos entero (int), en este variante de funcion
    se maneja el uso de una excepcion para el ingreso de datos que no son numericos:
    ------------
        No Recibe parametros de entrada
    
    Retorna:
    ------------
        Retorna un valor entero (numero) que es el dato ingresado transformado a (int)
    """
    while True:
        num = input()
        try:
            num = int(num)
            if num >=0 and num < 21:
                return num
            else:
                print("Solo valores entre 1 y 20")    
        except ValueError:
            print("Entrada No Valida")   

def salir():
    print("Gracias por utilizar el programa. SALIENDO...")
    time.sleep(2)
    os.system('cls')
    exit()

def menuOpciones():
        """
        Es un procedimiento que imprime un menu de opciones de transporte y recibe por
        teclado dos opciones que corresponderan al punto de partida y de entrega respectivamente
        del dron, esta validado con la funcion validarNumeros() para recibir solo valores numericos
        entre 0 y 20 y se fusiona con otra funcion que conecta al algoritmo de busqueda:
        ------------
            No Recibe parametros de entrada
        
        Retorna:
        ------------
            No retorna ningun valor
        """
        print("---Bienvenido al Sistema de Mensajeria ESPE---")
        print("A continuacion se presentan las ubicaciones disponibles para la recoleccion y entrega de mensajeria:")
        print("")
        print("1.- ENTRADA PRINCIPAL")
        print("2.- BIBLIOTECA")
        print("3.- EDIFICIO ADMINISTRATIVO")
        print("4.- EDIFICIO CENTRAL")
        print("5.- LABORATORIO MECANICA")
        print("6.- BLOQUE D")
        print("7.- BLOQUE C")
        print("8.- BLOQUE B")
        print("9.- BLOQUE A")
        print("10.- BAR")
        print("11.- ZONA DEPORTIVA")
        print("12.- ADUFA")
        print("13.- INNOVATIVA")
        print("14.- CENTRO DE INVESTIGACIONES")
        print("15.- LABORATORIO ELECTRONICA")
        print("16.- LABORATORIO AUTOMATIZACION")
        print("17.- LABORATORIO FLUIDOS")
        print("18.- LABORATORIO BIOTECNOLOGIA")
        print("19.- LABORATORIOS")
        print("20.- COLISEO")
        print("")
        print("Digite '0' para salir....")
        print("Ingrese el Lugar de recoleccion del paquete: ")
        opcion1 = validarNumeros()
        if opcion1 ==0:
            salir()
        else:        
            print("Ingrese el Lugar de entrega del paquete: ")
            opcion2 = validarNumeros()
            seleccion(opcion1, opcion2)

def seleccion(opcion1, opcion2):
    """
        Es un procedimiento que asocia el menu de opciones con el algoritmo de busqueda,
        tomando los valores escritos en el menu y asociandolos en una lista con sus direcciones
        colocadas de acuerdo a los indices del menu:
        ------------
            No Recibe parametros de entrada
        
        Retorna:
        ------------
            No retorna ningun valor
    """
    grafo = grafoDef()
    ubicaciones = ["Entrada", "Biblioteca", "Ed_Administrativo", "Ed_Central", "Lab_Mecanica",  "Bloque_D", "Bloque_C", "Bloque_B", "Bloque_A", "Bar",
        "Zona_Deportiva", "Adufa", "Innovativa", "Centro_Investig", "Lab_Electronica", "Lab_Automatizacion", "Lab_Fluidos", "Lab_Biotec", "Laboratorios", "Coliseo"]

    origen = ubicaciones[opcion1-1]
    destino = ubicaciones[opcion2-1]

    caminoCorto(grafo, origen, destino)


def busqueda(grafo, inicio, fin):
    # Crear un diccionario para almacenar el costo más bajo conocido de cada nodo al inicio
    costos = {nodo: float('inf') for nodo in grafo}
    #Cada nodo se inicializa con un valor infinito con el proposito de poder almacenar el valor mas bajo en cada iteracion 
    costos[inicio] = 0
    #Costo del nodo inicial es 0
    # Crear un diccionario para almacenar el camino más corto conocido de cada nodo al inicio
    rutaCorta = {}
    
    nodosSiguientes = set(grafo.keys())
    #Se almacena todo el conjunto de nodos del grafo, accediendo al nombre de cada uno mediante el metodo keys()
    # Mientras haya nodos por visitar
    while nodosSiguientes:
        # Encontrar el nodo con el costo más bajo actual
        nodoActual= min(nodosSiguientes, key=lambda nodo: costos[nodo])
        
        # Si llegamos al nodo final, regresar el costo y el camino más corto
        if nodoActual == fin:
            return (costos[fin], rutaCorta)
        
        # Actualizar los costos y el camino más corto de los nodos vecinos
        for nodoVecino, costo in grafo[nodoActual].items():
            costoTotal = costos[nodoActual] + costo
            
            # Si encontramos un costo más bajo para el siguiente nodo, actualizar el costo y el camino
            if costoTotal < costos[nodoVecino]:
                costos[nodoVecino] = costoTotal
                rutaCorta[nodoVecino] = nodoActual
        
        # Marcar el nodo actual como visitado
        nodosSiguientes.remove(nodoActual)
    
    # Si no se puede encontrar un camino al nodo final, regresar None
    return None


# Definir una función para encontrar el camino más corto y el costo de transporte
def caminoCorto(grafo, inicio, fin):
    # Usar el algoritmo de Dijkstra para encontrar el camino más corto y el costo de transporte
    costo, camino = busqueda(grafo, inicio, fin)
    
    # Construir la ruta a través del camino más corto
    ruta = [fin]
    while fin != inicio:
        ruta.append(camino[fin])
        fin = camino[fin]
    ruta.reverse()
    
    # Imprimir el resultado
    print("La ruta que sigue el Dron para llegar desde", inicio, "hasta", ruta[-1], "es:")
    #Cada ruta se imprime con una flecha para indicar que fue recorrida
    print(" -> ".join(ruta), end=" ")
    print("y el costo de transporte es de", costo)

    while True:
        opcionSiNo = input("Desea Realizar otro envio? S = Si / N = No")
        if opcionSiNo.upper() == 'S':
            menuOpciones()
        elif opcionSiNo.upper() == 'N':
            salir()
        else:
            print("Opcion No Valida, Intenta Otra vez")

def grafoDef():
    # Definir el grafo que representa la red de caminos entre las ubicaciones
    grafo = {
        "Entrada": {"Ed_Administrativo": 2, "Biblioteca": 2, "Ed_Central": 2},
        "Biblioteca": {"Entrada": 2 ,"Ed_Administrativo": 2, "Lab_Mecanica": 2},
        "Ed_Administrativo": {"Entrada": 2, "Biblioteca": 2 , "Ed_Central": 2, "Bloque_B": 2, "Bloque_C": 2},
        "Ed_Central": {"Entrada": 2, "Ed_Administrativo": 2, "Bloque_A": 2, "Bloque_B": 2, "Bar": 2, "Zona_Deportiva": 2, "Coliseo": 2},
        "Lab_Mecanica": {"Biblioteca": 2,"Bloque_D": 2},
        "Bloque_A" : {"Ed_Central": 2, "Bar": 2, "Bloque_B": 2, "Adufa": 2, "Lab_Electronica": 2},
        "Bloque_B" : {"Ed_Central" : 2, "Ed_Administrativo": 2, "Bloque_A": 2, "Bloque_C": 2, "Lab_Automatizacion": 2},
        "Bloque_C" : {"Ed_Administrativo": 2, "Bloque_B": 2, "Bloque_D": 2, "Lab_Fluidos": 2},
        "Bloque_D" : {"Lab_Mecanica": 2, "Bloque_C": 2, "Lab_Biotec": 2},
        "Bar" : {"Ed_Central": 2, "Bloque_A": 2, "Adufa": 2, "Zona_Deportiva": 2},
        "Zona_Deportiva" : {"Ed_Central": 2, "Bar": 2, "Coliseo": 2},
        "Adufa" : {"Bar": 2, "Bloque_A": 2, "Innovativa": 2, "Lab_Electronica": 2},
        "Coliseo" : {"Ed_Central": 2, "Zona_Deportiva": 2},
        "Innovativa" : {"Adufa": 2, "Centro_Investig": 2, "Lab_Electronica": 2},
        "Centro_Investig" : {"Innovativa": 2},
        "Lab_Biotec" : {"Bloque_D": 2, "Laboratorios": 2},
        "Laboratorios" : {"Lab_Biotec": 2, "Lab_Fluidos": 2},
        "Lab_Fluidos" : {"Bloque_C": 2, "Laboratorios": 2, "Lab_Automatizacion": 2},
        "Lab_Automatizacion" : {"Bloque_B": 2, "Lab_Fluidos": 2, "Lab_Electronica": 2},
        "Lab_Electronica" : {"Bloque_A": 2, "Lab_Automatizacion": 2, "Adufa": 2, "Innovativa": 2}
    }
    return grafo

if __name__ == '__main__':

    menuOpciones()

