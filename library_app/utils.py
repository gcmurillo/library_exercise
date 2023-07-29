from datetime import date

def validarOpcion(opciones, entrada):
  return entrada in opciones


def ingresarString(mensaje):
    entrada = input(mensaje)
    while (not len(entrada.strip())):
        entrada = input(mensaje)
    return entrada.strip()


def ingresarFecha(mensaje):
    while True:
        try:
            entrada = input(mensaje + "(dd-MM-YYYY): ").split("-")
            dia, mes, anio = [int(item) for item in entrada]
            d = date(anio, mes, dia)
            return d
        except:
            continue

   