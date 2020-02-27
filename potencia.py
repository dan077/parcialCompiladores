import sys

obtenerValores = sys.argv[1:]

def obtenerLenguaje(lenguaje):
    lenguaje = lenguaje[3:];
    elementos=lenguaje.split(",");
    elementos[-1] = elementos[-1].replace("}","")
    return elementos;

print(obtenerLenguaje(str(obtenerValores[0])));

