import matplotlib.pyplot as plt
from pathlib import Path

allValues = { 0: {}, 1: {} }

allValues[0][0] = {}
allValues[0][1] = {}
allValues[1][0] = {}
allValues[1][1] = {}

def graficar_todos():
    graficar_15w()
    graficar_7w()

    graficar_cpp()
    graficar_python()
    
def graficar_15w():
    
    plt.figure(figsize=(12, 6)) 
    plt.ylim(0,150)
    mean_list = [sum(allValues[0][0][0])/len(allValues[0][1][0]),
                 sum(allValues[0][0][2])/len(allValues[0][1][2]), 
                 sum(allValues[0][0][1])/len(allValues[0][1][1]),
                 sum(allValues[1][0][0])/len(allValues[1][1][0]),
                 sum(allValues[1][0][2])/len(allValues[1][1][2]),
                 sum(allValues[1][0][1])/len(allValues[1][1][1])
                 ]

    plt.bar(['Python-yolov8m', 'Python-yolov8s', 'Python-yolov8n', 'C++-yolov8m', 'C++-yolov8s','C++-yolov8n'], 
            mean_list,    
            color=['red', 'blue', 'green', 'purple','yellow', 'orange'], width=0.5)
    
    plt.title('Tiempo de inferencia en 15W' )
    plt.xlabel('Red y Lenguaje Usados')
    plt.ylabel('Tiempo de inferencia (ms)')
    
    plt.legend()
    plt.savefig('15wTime.png')
    #plt.show()
    plt.clf()

def graficar_7w():

    plt.figure(figsize=(12, 6)) 
    plt.ylim(0,150)
    mean_list = [sum(allValues[0][1][0])/len(allValues[0][1][0]),
                 sum(allValues[0][1][2])/len(allValues[0][1][2]), 
                 sum(allValues[0][1][1])/len(allValues[0][1][1]),
                 sum(allValues[1][1][0])/len(allValues[1][1][0]),
                 sum(allValues[1][1][2])/len(allValues[1][1][2]),
                 sum(allValues[1][1][1])/len(allValues[1][1][1])]
    #mean_list.sort()

    plt.bar(['Python-yolov8m', 'Python-yolov8s','Python-yolov8n', 'C++-yolov8m', 'C++-yolov8s', 'C++-yolov8n'], 
            mean_list,    
            color=['red', 'blue', 'green', 'purple','yellow', 'orange'], width=0.5)
    
    plt.title('Tiempo de inferencia en 7W' )
    plt.xlabel('Red y Lenguaje Usados')
    plt.ylabel('Tiempo de inferencia (ms)')
    
    plt.legend()
    plt.savefig('7wTime.png')
    #plt.show()
    plt.clf()

def graficar_cpp():

    plt.figure(figsize=(12, 6)) 
    plt.ylim(0,150)
    mean_list = [sum(allValues[1][0][0])/len(allValues[1][0][0]),
                 sum(allValues[1][0][2])/len(allValues[1][0][2]), 
                 sum(allValues[1][0][1])/len(allValues[1][0][1]),
                 sum(allValues[1][1][0])/len(allValues[1][1][0]),
                 sum(allValues[1][1][2])/len(allValues[1][1][2]),
                 sum(allValues[1][1][1])/len(allValues[1][1][1])]

    plt.bar(['15W-yolov8m', '15W-yolov8s', '15W-yolov8n', '7W-yolov8m', '7W-yolov8s', '7W-yolov8n'], 
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

    plt.figure(figsize=(12, 6)) 
    plt.ylim(0,150)
    mean_list = [sum(allValues[0][0][0])/len(allValues[0][0][0]), 
                 sum(allValues[0][0][2])/len(allValues[0][0][2]), 
                 sum(allValues[0][0][1])/len(allValues[0][0][1]),
                 sum(allValues[0][1][0])/len(allValues[0][1][0]),
                 sum(allValues[0][1][2])/len(allValues[0][1][2]),
                 sum(allValues[0][1][1])/len(allValues[0][1][1])]
    #mean_list.sort()

    plt.bar(['15W-yolov8m', '15W-yolov8s', '15W-yolov8n', '7W-yolov8m', '7W-yolov8s', '7W-yolov8n'], 
            mean_list,    
            color=['red', 'blue', 'green', 'purple','yellow', 'orange'], width=0.5)
    
    plt.title('Tiempo de inferencia en Python' )
    plt.xlabel('Red y Modo de Energía Usados')
    plt.ylabel('Tiempo de inferencia (ms)')
    
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

def leer_datos_python(ruta):
    f = open(ruta, "r")

    text = f.read()

    timeList = []

    lines = text.split('\n')

    for line in lines[22:-1]:
        if 'Speed' in line:
            splitLine = line.split(' ')
            timeList.append(float(splitLine[1].split('m')[0]) + float(splitLine[3].split('m')[0]) + float(splitLine[5].split('m')[0]))

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
    ruta = Path(ruta_carpeta)
    
    for elemento in ruta.iterdir():
        if elemento.is_dir():
            listar_archivos_y_subcarpetas(elemento)
        elif elemento.is_file():

            if('time' in elemento.name ):
                ruta = str(ruta_carpeta) + '/' + elemento.name
                print("Archivo: " + ruta)
                if 'c++' in ruta :
                    leer_datos(ruta)
                elif 'Python' in ruta:
                    leer_datos_python(ruta)

listar_archivos_y_subcarpetas('./scriptResult/')
graficar_todos()
