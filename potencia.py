import sys

obtenerValores = sys.argv[1:]
objetoVacio = "#"

def obtenerLenguaje(lenguaje):
    lenguaje = lenguaje[3:];
    elementos=lenguaje.split(",");
    elementos[-1] = elementos[-1].replace("}","")
    return elementos;

def obtenerPotencia(potencia):
    potencia = potencia[2:]
    portencia = int(potencia);
    return potencia

def obtenerVista(vista):
    vista = vista[0]
    return vista;

def potencia(elementos,potencia):
    if(potencia == 0):
        return ["#"]
    elif(potencia == 1):
        return elementos
    else:
        vectorInicial = elementos;
        vectorAux1 = elementos;
        vectorAux2 = []
        resultadoPotencia = []
        resultadoPotencia.append(["#"]); resultadoPotencia.append(elementos)
        for i in range(potencia -1):
            for q in vectorInicial:
                for x in vectorAux1:
                    vectorAux2.append(str(q)+str(x))
            resultadoPotencia.append(vectorAux2);
            vectorAux1 = vectorAux2;
            vectorAux2 = [];
        return  resultadoPotencia;


elementos = obtenerLenguaje(obtenerValores[0]);
potencias = obtenerPotencia(obtenerValores[1]);
vista = obtenerVista(obtenerValores[2]);

print(potencia(elementos,int(potencias)))






        
