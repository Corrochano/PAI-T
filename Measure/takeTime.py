import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

allValues = { 0: {}, 1: {} }

allValues[0][0] = {}
allValues[0][1] = {}
allValues[1][0] = {}
allValues[1][1] = {}

distanceValues = { 0: {}, 1: {} }

distanceValues[0][0] = {}
distanceValues[0][1] = {}
distanceValues[1][0] = {}
distanceValues[1][1] = {}

captureValues = { 0: {}, 1: {} }

captureValues[0][0] = {}
captureValues[0][1] = {}
captureValues[1][0] = {}
captureValues[1][1] = {}

inferenceValues = { 0: {}, 1: {} }

inferenceValues[0][0] = {}
inferenceValues[0][1] = {}
inferenceValues[1][0] = {}
inferenceValues[1][1] = {}

def graficar_todos():
    #graficar_15w()
    #graficar_7w()

    graficar_cpp()
    #graficar_python()

    graficar_cpp_capture()
    graficar_cpp_distance()
    graficar_cpp_inference()

    graficar_comparacion()
    
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
    
    plt.title('Tiempo total en C++' )
    plt.xlabel('Red y Modo de Energía Usados')
    plt.ylabel('Tiempo total (ms)')
    
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

def graficar_cpp_distance():

    plt.figure(figsize=(12, 6)) 
    plt.ylim(0,150)
    mean_list = [sum(distanceValues[1][0][0])/len(distanceValues[1][0][0]),
                 sum(distanceValues[1][0][2])/len(distanceValues[1][0][2]), 
                 sum(distanceValues[1][0][1])/len(distanceValues[1][0][1]),
                 sum(distanceValues[1][1][0])/len(distanceValues[1][1][0]),
                 sum(distanceValues[1][1][2])/len(distanceValues[1][1][2]),
                 sum(distanceValues[1][1][1])/len(distanceValues[1][1][1])]

    plt.bar(['15W-yolov8m', '15W-yolov8s', '15W-yolov8n', '7W-yolov8m', '7W-yolov8s', '7W-yolov8n'], 
            mean_list,    
            color=['red', 'blue', 'green', 'purple','yellow', 'orange'], width=0.5)
    
    plt.title('Tiempo de distancia en C++' )
    plt.xlabel('Red y Modo de Energía Usados')
    plt.ylabel('Tiempo de distancia (ms)')
    
    #plt.legend()
    plt.savefig('cppTimeDistance.png')
    #plt.show()
    plt.clf()

def graficar_cpp_capture():

    plt.figure(figsize=(12, 6)) 
    plt.ylim(0,150)
    mean_list = [sum(captureValues[1][0][0])/len(captureValues[1][0][0]),
                 sum(captureValues[1][0][2])/len(captureValues[1][0][2]), 
                 sum(captureValues[1][0][1])/len(captureValues[1][0][1]),
                 sum(captureValues[1][1][0])/len(captureValues[1][1][0]),
                 sum(captureValues[1][1][2])/len(captureValues[1][1][2]),
                 sum(captureValues[1][1][1])/len(captureValues[1][1][1])]

    plt.bar(['15W-yolov8m', '15W-yolov8s', '15W-yolov8n', '7W-yolov8m', '7W-yolov8s', '7W-yolov8n'], 
            mean_list,    
            color=['red', 'blue', 'green', 'purple','yellow', 'orange'], width=0.5)
    
    plt.title('Tiempo de captura en C++' )
    plt.xlabel('Red y Modo de Energía Usados')
    plt.ylabel('Tiempo de captura (ms)')
    
    #plt.legend()
    plt.savefig('cppTimeCapture.png')
    #plt.show()
    plt.clf()

def graficar_cpp_inference():

    plt.figure(figsize=(12, 6)) 
    plt.ylim(0,150)
    mean_list = [sum(inferenceValues[1][0][0])/len(inferenceValues[1][0][0]),
                 sum(inferenceValues[1][0][2])/len(inferenceValues[1][0][2]), 
                 sum(inferenceValues[1][0][1])/len(inferenceValues[1][0][1]),
                 sum(inferenceValues[1][1][0])/len(inferenceValues[1][1][0]),
                 sum(inferenceValues[1][1][2])/len(inferenceValues[1][1][2]),
                 sum(inferenceValues[1][1][1])/len(inferenceValues[1][1][1])]

    plt.bar(['15W-yolov8m', '15W-yolov8s', '15W-yolov8n', '7W-yolov8m', '7W-yolov8s', '7W-yolov8n'], 
            mean_list,    
            color=['red', 'blue', 'green', 'purple','yellow', 'orange'], width=0.5)
    
    plt.title('Tiempo de captura en C++' )
    plt.xlabel('Red y Modo de Energía Usados')
    plt.ylabel('Tiempo de captura (ms)')
    
    #plt.legend()
    plt.savefig('cppTimeInference.png')
    #plt.show()
    plt.clf()

def graficar_comparacion():
    plt.figure(figsize=(12, 6)) 
    plt.ylim(0,150)

    X = ['15W-yolov8m', '15W-yolov8s', '15W-yolov8n', '7W-yolov8m', '7W-yolov8s', '7W-yolov8n'] 
    distance = [sum(distanceValues[1][0][0])/len(distanceValues[1][0][0]),
                 sum(distanceValues[1][0][2])/len(distanceValues[1][0][2]), 
                 sum(distanceValues[1][0][1])/len(distanceValues[1][0][1]),
                 sum(distanceValues[1][1][0])/len(distanceValues[1][1][0]),
                 sum(distanceValues[1][1][2])/len(distanceValues[1][1][2]),
                 sum(distanceValues[1][1][1])/len(distanceValues[1][1][1])]
    
    capture = [sum(captureValues[1][0][0])/len(captureValues[1][0][0]),
                 sum(captureValues[1][0][2])/len(captureValues[1][0][2]), 
                 sum(captureValues[1][0][1])/len(captureValues[1][0][1]),
                 sum(captureValues[1][1][0])/len(captureValues[1][1][0]),
                 sum(captureValues[1][1][2])/len(captureValues[1][1][2]),
                 sum(captureValues[1][1][1])/len(captureValues[1][1][1])]
    
    inference = [sum(inferenceValues[1][0][0])/len(inferenceValues[1][0][0]),
                 sum(inferenceValues[1][0][2])/len(inferenceValues[1][0][2]), 
                 sum(inferenceValues[1][0][1])/len(inferenceValues[1][0][1]),
                 sum(inferenceValues[1][1][0])/len(inferenceValues[1][1][0]),
                 sum(inferenceValues[1][1][2])/len(inferenceValues[1][1][2]),
                 sum(inferenceValues[1][1][1])/len(inferenceValues[1][1][1])]
    


    ind = np.arange(len(X))  
    width = 0.25
    
    plt.bar(ind, distance, width, color = 'r', label = 'Tiempo de Distancia') 
    plt.bar(ind+width, capture, width, color='g', label = 'Tiempo de captura') 
    plt.bar(ind+width*2, inference, width, color = 'b', label = 'Tiempo de inferencia') 

    plt.xticks(ind, X) 
    plt.xlabel("Modelos de YOLO") 
    plt.ylabel("Tiempo (ms)") 
    plt.title("Comparación de tiempos por acción") 
    
    plt.legend()
    plt.savefig('cppTimeComparation.png')
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

def leer_datos_best(ruta):
    f = open(ruta, "r")

    text = f.read()

    captureTimeList = []
    inferenceTimeList = []
    distanceTimeList = []
    totalTimeList = []

    lines = text.split('\n')

    for line in lines[:-1]:
        if 'Distance' in line:
            distanceTimeList.append(float(line.split(':')[1]))
        if 'Capture' in line:
            captureTimeList.append(float(line.split(':')[1]))
        if 'Inference' in line:
            inferenceTimeList.append(float(line.split(':')[1]))
        if 'Total' in line:
            totalTimeList.append(float(line.split(':')[1]))

    f.close()

    # Siempre C++
    if '15' in ruta:
        if('yolov8m' in ruta):
            allValues[1][0][0] = totalTimeList
            distanceValues[1][0][0] = distanceTimeList
            captureValues[1][0][0] = captureTimeList
            inferenceValues[1][0][0] = inferenceTimeList
        elif('yolov8n' in ruta):
            allValues[1][0][1] = totalTimeList
            distanceValues[1][0][1] = distanceTimeList
            captureValues[1][0][1] = captureTimeList
            inferenceValues[1][0][1] = inferenceTimeList
        elif('yolov8s' in ruta):
            allValues[1][0][2] = totalTimeList
            distanceValues[1][0][2] = distanceTimeList
            captureValues[1][0][2] = captureTimeList
            inferenceValues[1][0][2] = inferenceTimeList
    elif '7' in ruta:
        if('yolov8m' in ruta):
            allValues[1][1][0] = totalTimeList
            distanceValues[1][1][0] = distanceTimeList
            captureValues[1][1][0] = captureTimeList
            inferenceValues[1][1][0] = inferenceTimeList
        elif('yolov8n' in ruta):
            allValues[1][1][1] = totalTimeList
            distanceValues[1][1][1] = distanceTimeList
            captureValues[1][1][1] = captureTimeList
            inferenceValues[1][1][1] = inferenceTimeList
        elif('yolov8s' in ruta):
            allValues[1][1][2] = totalTimeList
            distanceValues[1][1][2] = distanceTimeList
            captureValues[1][1][2] = captureTimeList
            inferenceValues[1][1][2] = inferenceTimeList

def listar_archivos_y_subcarpetas(ruta_carpeta):
    ruta = Path(ruta_carpeta)
    
    for elemento in ruta.iterdir():
        if elemento.is_dir():
            listar_archivos_y_subcarpetas(elemento)
        elif elemento.is_file():

            if('time' in elemento.name ):
                ruta = str(ruta_carpeta) + '/' + elemento.name
                print("Archivo: " + ruta)
                if 'best' in ruta:
                    leer_datos_best(ruta)
                elif 'c++' in ruta :
                    leer_datos(ruta)
                elif 'Python' in ruta:
                    leer_datos_python(ruta)

listar_archivos_y_subcarpetas('./scriptResult/')
graficar_todos()
