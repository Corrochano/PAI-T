import matplotlib.pyplot as plt
from pathlib import Path

allValues = { 0: {}, 1: {} }

allValues[0][0] = {}
allValues[0][1] = {}
allValues[1][0] = {}
allValues[1][1] = {}

def graficar_todos():
    #graficar_15w()
    #graficar_7w()

    graficar_cpp()
    #graficar_python()
    
def graficar_15w():
    
    # Generar la gráfica
    plt.plot(allValues[0][0][0], label='Python - yolov8m', color='#0000FF', linestyle='-')
    plt.plot(allValues[0][0][1], label='Python - yolov8n', color='#000099', linestyle=':')
    plt.plot(allValues[0][0][2], label='Python - yolov8s', color='#000055', linestyle='--')
    plt.plot(allValues[1][0][0], label='c++ - yolov8m', color='#FF0000', linestyle='-')
    plt.plot(allValues[1][0][1], label='c++ - yolov8n', color='#990000', linestyle=':')
    plt.plot(allValues[1][0][2], label='c++ - yolov8s', color='#550000', linestyle='--')
    
    plt.title('Tiempo de inferencia en 15w' )
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Consumo (mW)')
    
    plt.legend()
    plt.savefig('15wTime.png')
    #plt.show()
    plt.clf()

def graficar_7w():
    
    # Generar la gráfica
    plt.plot(allValues[0][1][0], label='Python - yolov8m', color='#0000FF', linestyle='-')
    plt.plot(allValues[0][1][1], label='Python - yolov8n', color='#000099', linestyle=':')
    plt.plot(allValues[0][1][2], label='Python - yolov8s', color='#000055', linestyle='--')
    plt.plot(allValues[1][1][0], label='c++ - yolov8m', color='#FF0000', linestyle='-')
    plt.plot(allValues[1][1][1], label='c++ - yolov8n', color='#990000', linestyle=':')
    plt.plot(allValues[1][1][2], label='c++ - yolov8s', color='#550000', linestyle='--')
    
    plt.title('Consumo energético en 7w' )
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Consumo (mW)')
    
    plt.legend()
    plt.savefig('7wTime.png')
    #plt.show()
    plt.clf()

def graficar_cpp():

    plt.figure(figsize=(12, 6)) 
    
    mean_list = [sum(allValues[1][0][0])/len(allValues[1][0][0]), sum(allValues[1][0][1])/len(allValues[1][0][1]),
             sum(allValues[1][0][2])/len(allValues[1][0][2]), 
             sum(allValues[1][1][0])/len(allValues[1][1][0]), sum(allValues[1][1][1])/len(allValues[1][1][1]),
             sum(allValues[1][1][2])/len(allValues[1][1][2])]
    #mean_list.sort()

    plt.bar(['15W-yolov8m', '15W-yolov8n', '15W-yolov8s', '7W-yolov8m', '7W-yolov8n', '7W-yolov8s'], 
            mean_list,    
            color=['red', 'blue', 'green', 'purple','yellow', 'orange'], width=0.5)
    
    plt.title('Tiempo de inferencia en C++' )
    plt.xlabel('Red y Modo de Energía Usados')
    plt.ylabel('Tiempo de inferencia (ms)')
    
    #plt.legend()
    plt.savefig('cppTime.png')
    #plt.show()
    plt.clf()

def graficar_python():
    
    # Generar la gráfica
    plt.plot(allValues[0][0][0], label='15W - yolov8m', color='#0000FF', linestyle='-')
    plt.plot(allValues[0][0][1], label='15W - yolov8n', color='#000099', linestyle=':')
    plt.plot(allValues[0][0][2], label='15W - yolov8s', color='#000055', linestyle='--')
    plt.plot(allValues[0][1][0], label='7W - yolov8m', color='#FF0000', linestyle='-')
    plt.plot(allValues[0][1][1], label='7W - yolov8n', color='#990000', linestyle=':')
    plt.plot(allValues[0][1][2], label='7W - yolov8s', color='#550000', linestyle='--')
    
    plt.title('Consumo energético en Python' )
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Consumo (mW)')
    
    plt.legend()
    plt.savefig('pythonTime.png')
    #plt.show()
    plt.clf()

def leer_datos(ruta):
    f = open(ruta, "r")

    text = f.read()

    timeList = []

    lines = text.split('\n')

    for line in lines[11:-1]:
        timeList.append(float(line))

    f.close()

    maxV = max(timeList)
    minV = min(timeList)
    meanV = sum(timeList) / len(timeList) 

    print(maxV)
    print(minV)
    print(meanV)

    if 'Python' in ruta:
        if '15' in ruta:
            if('yolov8m' in ruta):
                allValues[0][0][0] = timeList
            elif('yolov8n' in ruta):
                allValues[0][0][1] = timeList
            elif('yolov8s' in ruta):
                allValues[0][0][2] = timeList
        elif '7' in ruta:
            if('yolov8m' in ruta):
                allValues[0][1][0] = timeList
            elif('yolov8n' in ruta):
                allValues[0][1][1] = timeList
            elif('yolov8s' in ruta):
                allValues[0][1][2] = timeList
    elif 'c++' in ruta:
        if '15' in ruta:
            if('yolov8m' in ruta):
                allValues[1][0][0] = timeList
            elif('yolov8n' in ruta):
                allValues[1][0][1] = timeList
            elif('yolov8s' in ruta):
                allValues[1][0][2] = timeList
        elif '7' in ruta:
            if('yolov8m' in ruta):
                allValues[1][1][0] = timeList
            elif('yolov8n' in ruta):
                allValues[1][1][1] = timeList
            elif('yolov8s' in ruta):
                allValues[1][1][2] = timeList


def listar_archivos_y_subcarpetas(ruta_carpeta):
    # Crear un objeto Path para la ruta dada
    ruta = Path(ruta_carpeta)
    
    # Iterar sobre todos los elementos dentro de la carpeta
    for elemento in ruta.iterdir():
        # Comprobar si es un directorio (subcarpeta) o un archivo
        if elemento.is_dir():
            #print(f"Subcarpeta encontrada: {elemento.name}")
            # Llamar recursivamente a esta función para las subcarpetas
            listar_archivos_y_subcarpetas(elemento)
        elif elemento.is_file():
            #print(f"Archivo encontrado: {elemento.name}")

            if('time' in elemento.name ):
                ruta = str(ruta_carpeta) + '/' + elemento.name
                if 'c++' in ruta :
                    print("Archivo: " + ruta)
                    leer_datos(ruta)

listar_archivos_y_subcarpetas('./Measure')
graficar_todos()
