import sys

obtenerValores = sys.argv[1:]


def obtenerLenguaje(lenguaje):
    lenguaje = lenguaje[3:];
    elementos = lenguaje.split(",");
    elementos[-1] = elementos[-1].replace("}", "")
    return elementos;


def obtenerPotencia(potencia):
    potencia = potencia[2:]
    portencia = int(potencia);
    return potencia


def obtenerVista(vista):
    vista = vista[0]
    return vista;


elementos = obtenerLenguaje(obtenerValores[0]);
potencia = obtenerPotencia(obtenerValores[1]);
vista = obtenerVista(obtenerValores[2]);


def productoCruz(elementos):
    vectores = []
    texto = "";
    if (vista == "-"):
        if (potencia == 0):
            print("#");
        else:
            for i in range(potencia):

                for q in i * 2:
                    texto += elementos[i] + elementos[q]



    else:
        if (potencia == 0):
            print("L1 = #");