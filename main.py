from random import randint

# Constantes

MENU = ["Total de la facturación del mes y cantidad de socios",
        "Total de facturación por tipo de socio y la cantidad de actividades"
        "ordenado por facturación",
        "Listado completo detallado del total facturado de cada socio"
        "con su tipo, ordenado por el total facturado",
        "Seleccion de socio",
        "Salir",
        ]
TIPO_SOCIO = ["Junior", "Standar", "Platino", "Oro", "Vitalicio"]
CAT_CANT_ACT = ["0", "hasta 2", "mas de 3"]
COSTOS = [
    [750, 1500, 1000],
    [3000, 2500, 1500],
    [2300, 1500, 1300],
    [1900, 1500, 1300],
    [0, 1000, 750]
]

# Metodos generales


def mostrar_menu(options: []) -> None:
    contador = 1

    for opcion in options:
        print(contador, opcion)
        contador += 1


def generar_factura(tipo_socio, cant_activades):
    cuota_social = COSTOS[tipo_socio][0]
    valor_por_actividad = None

    if cant_activades >= 3:
        valor_por_actividad = 1
    else:
        valor_por_actividad = 2

    return cuota_social + (COSTOS[tipo_socio][valor_por_actividad] * cant_activades)


def generar_socios(min, max):
    socios = []
    cantidad_generar = randint(min, max)
    id_socio = 0

    for _ in range(cantidad_generar):
        socio = []
        tipo_socio = randint(0, 4)
        cant_actividades = randint(0, 6)
        facturacion = generar_factura(tipo_socio, cant_actividades)

        socio.append(id_socio)
        socio.append(tipo_socio)
        socio.append(cant_actividades)
        socio.append(facturacion)

        socios.append(socio)

        id_socio += 1

    return socios

#Ordena la matriz segun el campo cve indicado en orden descendente y la devuelve
def ordenar_matriz(matriz,cve): 
    for i in range (1, len(matriz)):
        aux = matriz[i]
        j = i
        while j > 0 and matriz[j-1][cve] < aux[cve]:
            matriz[j] = matriz[j-1]
            j = j - 1
        matriz[j] = aux
    return matriz

#Ordena el vector y lo devuelve ordenado
def ordenar_vector(vector): 
    for i in range (1, len(vector)):
        aux = vector[i]
        j = i
        while j > 0 and vector[j-1] < aux:
            vector[j] = vector[j-1]
            j = j - 1
        vector[j] = aux
    return vector

#Crea un vector auxiliar las posiciones del vector ordenados por facturacion en orden descendente y lo devuelve
def vec_ord_vec(vector): 
    vec = []
    for i in range (0, len(vector)):
        vec.append(i)
    for i in range (1, len(vector)):
        aux = vec[i]
        j = i
        while j > 0 and vector[vec[j-1]] < vector[aux]:
            vec[j] = vec[j-1]
            j = j - 1
        vec[j] = aux
    return vec

#Crea un vector auxiliar con los ids de la matriz ordenados por facturacion en orden descendente
def vec_ord_matriz_con_id(matriz,id_socio,cve_ord): 
    vec = []
    for i in range (0, len(matriz)):
        vec.append(matriz[i][id_socio])
    for i in range (1, len(matriz)):
        aux = vec[i]
        j = i
        while j > 0 and matriz[vec[j-1]][cve_ord] < matriz[aux][cve_ord]:
            vec[j] = vec[j-1]
            j = j - 1
        vec[j] = aux
    return vec

#Crea un vector auxiliar con las posiciones de la matriz ordenados por el campo cve pedido en orden descendente y lo devuelve
def vec_ord_matriz(matriz,cve_ord): 
    vec = []
    for i in range (0, len(matriz)):
        vec.append(i)
    for i in range (1, len(matriz)):
        aux = vec[i]
        j = i
        while j > 0 and matriz[vec[j-1]][cve_ord] < matriz[aux][cve_ord]:
            vec[j] = vec[j-1]
            j = j - 1
        vec[j] = aux
    return vec

#Crea y devuelve un array relleno con 0's con la cantidad de filas y columnas pedidas
def crear_arreglo_con_0(filas,columnas): 
    matriz = []
    for f in range(filas):
        if columnas == (1):
            matriz.append(0)
        else:
            matriz.append([])
            for c in range(columnas):
                matriz[f].append(0)
    return matriz


# Consigna 1


def total_facturacion_mes(socios: []) -> None:
    # return [total_facturacion, cantidad_socios] -> [int, int]

    return None

# Consigna 2

def calcular_fac_tot_por_tipo_socio(matriz):
    #Se crean las matrices acumuladoras inicializadas en 0
    fact_por_act = crear_arreglo_con_0(5,3)
    fact_tot = crear_arreglo_con_0(5,1)
    #Se comienza el ciclo en el cual se recorre la matriz sumando los facturados
    for i in range(len(matriz)):
        #Se crea una variable catalogo que sirve para ver si el socio entra en la categoria
        #de 0 actividades, hasta 2 actividades o 3 o mas actividades
        cat_act = 0
        if 0 < matriz[i][2] <= 2:
            cat_act = 1
        elif matriz[i][2] > 2:
            cat_act = 2
        #Se realizan las sumas en las matrices acumuladoras
        fact_por_act[matriz[i][1]][cat_act] += matriz[i][3]
        fact_tot[matriz[i][1]] += matriz[i][3]
    #Se crea un vector orden segun el total facturado de mayor a menor
    orden_tot = vec_ord_vec(fact_tot)
    #Se recorre el vector de facturados totales por tipo de socio imprimiendo los tipos de socios
    for i in range(len(fact_tot)):
        print("Socios",TIPO_SOCIO[orden_tot[i]])
        #Se crea un vector orden segun el facturado por cantidad de actividades de mayor a menor
        orden_act = vec_ord_vec(fact_por_act[orden_tot[i]])
        #Se recorre el vector correspondiente a ese tipo de socio de la matriz facturado por cant de actividades
        for j in range(len(fact_por_act[orden_tot[i]])):
            print("Con",CAT_CANT_ACT[orden_act[j]],"actividades:", fact_por_act[orden_tot[i]][orden_act[j]])


# Consigna 3


def listado_detallado_socios(socios: []) -> None:

    return None

# Consigna 4


def detalle_socio_por_tipo(socios: []) -> None:

    return None


def manejar_opciones(opcion, socios) -> None:
    print("\n")

    if opcion == 1:
        total_facturacion_mes(socios)
    elif opcion == 2:
        print("Opción 2")
    elif opcion == 3:
        listado_detallado_socios(socios)
    elif opcion == 4:
        detalle_socio_por_tipo(socios)
    elif opcion == 5:
        print("Gracias por usar el programa")
    else:
        print("Opción incorrecta")

# Funcion principal


def main() -> None:
    socios = generar_socios(100, 1000)
    option = None

    mostrar_menu(MENU)

    while option != 5:
        option = int(input("Ingrese una opción: "))

        manejar_opciones(option, socios)


main()
