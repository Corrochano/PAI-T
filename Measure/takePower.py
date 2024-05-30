import matplotlib.pyplot as plt
from pathlib import Path

model = 'yolov8n'
watios = '7'

allValues = { 0: {}, 1: {} }

allValues[0][0] = {}
allValues[0][1] = {}
allValues[1][0] = {}
allValues[1][1] = {}

def graficar_lista(valores):
    # Crear los ejes x e y
    x = range(len(valores))
    y = valores
    
    # Generar la gráfica
    plt.plot(x, y)
    
    # rango y
    plt.ylim(min(y) - 50, max(y) + 50)

    # Agregar títulos y etiquetas
    plt.title('Consumo energético de ' + model + 'en ' + watios)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Consumo (mW)')

def graficar_todos():
    graficar_15w()
    graficar_7w()

    graficar_cpp()
    graficar_python()
    
def graficar_15w():

    plt.figure(figsize=(12, 6)) 
    
    # Generar la gráfica
    plt.plot(allValues[0][0][0], label='Python - yolov8m', color='#0000FF', linestyle='-')
    plt.plot(allValues[0][0][1], label='Python - yolov8n', color='#000099', linestyle=':')
    plt.plot(allValues[0][0][2], label='Python - yolov8s', color='#000055', linestyle='--')
    plt.plot(allValues[1][0][0], label='c++ - yolov8m', color='#FF0000', linestyle='-')
    plt.plot(allValues[1][0][1], label='c++ - yolov8n', color='#990000', linestyle=':')
    plt.plot(allValues[1][0][2], label='c++ - yolov8s', color='#550000', linestyle='--')
    
    plt.title('Consumo energético en 15w' )
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Consumo (mW)')
    
    plt.legend()
    plt.savefig('15w.png')
    #plt.show()
    plt.clf()

def graficar_7w():

    plt.figure(figsize=(12, 6)) 
    
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
    plt.savefig('7w.png')
    #plt.show()
    plt.clf()

def graficar_cpp():
    plt.figure(figsize=(12, 6)) 
    
    # Generar la gráfica
    plt.plot(allValues[1][0][0], label='15W - yolov8m', color='#0000FF', linestyle='-')
    plt.plot(allValues[1][0][1], label='15W - yolov8n', color='#000099', linestyle=':')
    plt.plot(allValues[1][0][2], label='15W - yolov8s', color='#000055', linestyle='--')
    plt.plot(allValues[1][1][0], label='7W - yolov8m', color='#FF0000', linestyle='-')
    plt.plot(allValues[1][1][1], label='7W - yolov8n', color='#990000', linestyle=':')
    plt.plot(allValues[1][1][2], label='7W - yolov8s', color='#550000', linestyle='--')
    
    plt.title('Consumo energético en C++' )
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Consumo (mW)')
    
    plt.legend()
    plt.savefig('cpp.png')
    #plt.show()
    plt.clf()

def graficar_python():
    plt.figure(figsize=(12, 6)) 
    
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
    plt.savefig('python.png')
    #plt.show()
    plt.clf()
    
def leer_datos(ruta):
    f = open(ruta, "r")

    text = f.read()

    powerList = []

    lines = text.split('\n')

    for line in lines[:-1]:
        line = line.split(' ')

        powerValue = line[-1].split('/')[0][:-2]

        powerList.append(float(powerValue))

    f.close()

    maxV = max(powerList)
    minV = min(powerList)
    meanV = sum(powerList) / len(powerList) 

    print(maxV)
    print(minV)
    print(meanV)

    #graficar_lista(powerList)
    if 'Python' in ruta:
        if '15' in ruta:
            if('yolov8m' in ruta):
                allValues[0][0][0] = powerList
            elif('yolov8n' in ruta):
                allValues[0][0][1] = powerList
            elif('yolov8s' in ruta):
                allValues[0][0][2] = powerList
        elif '7' in ruta:
            if('yolov8m' in ruta):
                allValues[0][1][0] = powerList
            elif('yolov8n' in ruta):
                allValues[0][1][1] = powerList
            elif('yolov8s' in ruta):
                allValues[0][1][2] = powerList
    elif 'c++' in ruta:
        if '15' in ruta:
            if('yolov8m' in ruta):
                allValues[1][0][0] = powerList
            elif('yolov8n' in ruta):
                allValues[1][0][1] = powerList
            elif('yolov8s' in ruta):
                allValues[1][0][2] = powerList
        elif '7' in ruta:
            if('yolov8m' in ruta):
                allValues[1][1][0] = powerList
            elif('yolov8n' in ruta):
                allValues[1][1][1] = powerList
            elif('yolov8s' in ruta):
                allValues[1][1][2] = powerList

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

            if(not 'time' in elemento.name ):
                ruta = str(ruta_carpeta) + '/' + elemento.name
                print("Archivo: " + ruta)
                ruta_list = ruta.split('/')

                model = ruta_list[2].split('.')[0]
                watios = ruta_list[1]
                if 'noidle' in ruta :
                    leer_datos(ruta)

# Ejemplo de uso
ruta_carpeta = './Measure/'
listar_archivos_y_subcarpetas(ruta_carpeta)

graficar_todos()