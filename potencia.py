import sys

obtenerValores = sys.argv[1:]

def obtenerLenguaje(lenguaje):
    lenguaje = lenguaje[3:];
    elementos=lenguaje.split(",");
    elementos[-1] = elementos[-1].replace("}","")
    return elementos;

def obtenerPotencia(potencia):
    potencia = potencia[2:]
    portencia = int(potencia);
    return potencia


print(obtenerLenguaje(obtenerValores[0]));
print(obtenerPotencia(obtenerValores[1]))

for i in range(len(elementos())):

    if (elementos[i] == '#'):
        
        c +=c+1
        print('#')

        
