from random import randint

MENU = ["Total de la facturación del mes y cantidad de socios",
        "Total de facturación por tipo de socio y la cantidad de actividades"
        "ordenado por facturación",
        "Listado completo detallado del total facturado de cada socio"
        "con su tipo, ordenado por el total facturado",
        "Seleccion de socio",
        "Salir",
        ]
TIPO_SOCIO = ["Junior", "Standar", "Platino", "Oro", "Vitalicio"]

# TODO: Juntar en un solo array.
# TODO: Renombrar a COSTOS
CUOTA_SOCIO = [750, 3000, 2300, 1900, 0]
VALORES_ACTIVIDADES = [
    [1500, 1000],
    [2500, 1500],
    [1500, 1300],
    [1500, 1300],
    [1000, 750],
]

# TODO: Crear variable contador
def mostrar_menu(options: []) -> None:
    for i, option in enumerate(options):
        print(i + 1, option)

# TODO: Agregar generador de id, contador
# TODO: Agregar facturacion

def generar_socios(min: int, max: int) -> []:
    socios = []
    cantidad_generar = randint(min, max)

    for i in range(cantidad_generar):
        socio = []
        socio.append(randint(0, 4))
        socio.append(randint(0, 6))

        socios.append(socio)

    return socios

# TODO: Agregar la multiplicacion por actividad
def calcular_valor_actividades(tipo_socio: int, cant_activades: int) -> int:
    valor_actividad = 0 if cant_activades >= 3 else 1

    return CUOTA_SOCIO[tipo_socio] + VALORES_ACTIVIDADES[tipo_socio][valor_actividad]

# Consigna 1

# TODO: Arreglar return, deberia ser [total_ingresos, cantidad de socios]
# TODO: Cambiar para usar la funcion generar_factura()

def total_facturacion_mes(socios: []) -> [int, int]:
    total_ingresos = 0

    for socio in socios:
        total_ingresos += calcular_valor_actividades(socio[0], socio[1])

    return [total_ingresos, len(socios)]


def main() -> None:
    socios = generar_socios(100, 1000)
    option = None

    mostrar_menu(MENU)

    while option != 5:
        option = int(input("Ingrese una opción: "))

        if option == 1:
            print(
                "Total de la facturación del mes:",
                total_facturacion_mes(socios)[0]
            )
            print("Cantidad de socios:", total_facturacion_mes(socios)[1])


main()
