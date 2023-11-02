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

#Crea un vector auxiliar con los ids de la matriz ordenados por facturacion en orden descendente
def vec_ord(matriz,id_socio,cve_ord):
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
    

# Consigna 1


def total_facturacion_mes(socios: []) -> None:
    # return [total_facturacion, cantidad_socios] -> [int, int]

    return None

# Consigna 2
# Pendiente. dependiendo de que diga la consigna

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
