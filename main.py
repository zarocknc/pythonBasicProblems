import os

from InquirerPy import inquirer


# FUNCIONES
def Ingrese(msg, tipo="str"):
    # return float(inquirer.number(message=msg, float_allowed=True).execute())
    # if tipo == "str":
    #     print("es un string")
    # elif tipo == "int":
    #     print("es un integrer")
    tipes = {
        "str": lambda msg: inquirer.text(message=msg).execute(),
        "int": lambda msg: int(inquirer.number(message=msg).execute()),
        "float": lambda msg: float(
            inquirer.number(message=msg, float_allowed=True).execute()
        ),
        "bool": lambda msg: inquirer.confirm(message=msg).execute(),
    }
    return tipes[tipo](msg)


barra = os.get_terminal_size().columns * "-"


# PROGRAMA 1 promedio de 4 numeros
print("PROGRAMA 1")
print("promedio de 4 numeros")
print(barra)
suma = 0
for i in range(1, 5):
    suma += Ingrese(f"ingrese el numero {i}:", "float")
print("la suma total es", suma)
print(f"el promedio es:", suma / 4)
