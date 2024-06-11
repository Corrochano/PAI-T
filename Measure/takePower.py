import matplotlib.pyplot as plt
from pathlib import Path

model = 'yolov8n'
watios = '7'

allValues = { 0: {}, 1: {} }

allValues[0][0] = {}
allValues[0][1] = {}
allValues[1][0] = {}
allValues[1][1] = {}

cpugpuValues = { 0: {}, 1: {} }

cpugpuValues[0][0] = {}
cpugpuValues[0][1] = {}
cpugpuValues[1][0] = {}
cpugpuValues[1][1] = {}

def graficar_lista(valores):
    # Crear los ejes x e y
    x = range(len(valores))
    y = valores
    
    # Generar la gráfica
    plt.plot(x, y)
    
    # rango y
    plt.ylim(1500, 2300)

    # Agregar títulos y etiquetas
    plt.title('Consumo energético de ' + model + 'en ' + watios)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Consumo (mW)')

def graficar_todos():
    #graficar_15w()
    #graficar_7w()

    #graficar_cpp()
    #graficar_python()

    #graficar_15w_barras()
    #graficar_7w_barras()

    graficar_cpp_barras()
    #graficar_python_barras()

    graficar_cpp_cpugpu_barras()
    
def graficar_15w():

    plt.figure(figsize=(12, 6)) 
    plt.ylim(1500, 2300)

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
    plt.ylim(1500, 2300)
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
    plt.ylim(1500, 2300)
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
    plt.ylim(1500, 2300)
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

def graficar_15w_barras():
    
    plt.figure(figsize=(12, 6)) 
    plt.ylim(1500, 2300)
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
    
    plt.title('Consumo Medio en 15W' )
    plt.xlabel('Red y Lenguaje Usados')
    plt.ylabel('Consumo (mW)')
    
    plt.legend()
    plt.savefig('15wBarras.png')
    #plt.show()
    plt.clf()

def graficar_7w_barras():

    plt.figure(figsize=(12, 6)) 
    plt.ylim(1500, 2300)
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
    
    plt.title('Consumo Medio en 7W' )
    plt.xlabel('Red y Lenguaje Usados')
    plt.ylabel('Consumo (mW)')
    
    plt.legend()
    plt.savefig('7wBarras.png')
    #plt.show()
    plt.clf()

def graficar_cpp_barras():

    plt.figure(figsize=(12, 6)) 
    plt.ylim(1500, 7000)
    mean_list = [sum(allValues[1][0][0])/len(allValues[1][0][0]),
                 sum(allValues[1][0][2])/len(allValues[1][0][2]), 
                 sum(allValues[1][0][1])/len(allValues[1][0][1]),
                 sum(allValues[1][1][0])/len(allValues[1][1][0]),
                 sum(allValues[1][1][2])/len(allValues[1][1][2]),
                 sum(allValues[1][1][1])/len(allValues[1][1][1])]

    plt.bar(['15W-yolov8m', '15W-yolov8s', '15W-yolov8n', '7W-yolov8m', '7W-yolov8s', '7W-yolov8n'], 
            mean_list,    
            color=['red', 'blue', 'green', 'purple','yellow', 'orange'], width=0.5)
    
    plt.title('Consumo Medio en C++ (Vin)' )
    plt.xlabel('Red y Modo Usados')
    plt.ylabel('Consumo (mW)')
    
    #plt.legend()
    plt.savefig('cppBarras.png')
    #plt.show()
    plt.clf()

def graficar_cpp_cpugpu_barras():

    #plt.figure(figsize=(12, 6)) 
    #plt.ylim(1500, 2000)
    mean_list = [sum(cpugpuValues[1][0][0])/len(cpugpuValues[1][0][0]),
                 sum(cpugpuValues[1][0][2])/len(cpugpuValues[1][0][2]), 
                 sum(cpugpuValues[1][0][1])/len(cpugpuValues[1][0][1]),
                 sum(cpugpuValues[1][1][0])/len(cpugpuValues[1][1][0]),
                 sum(cpugpuValues[1][1][2])/len(cpugpuValues[1][1][2]),
                 sum(cpugpuValues[1][1][1])/len(cpugpuValues[1][1][1])]

    plt.bar(['15W-yolov8m', '15W-yolov8s', '15W-yolov8n', '7W-yolov8m', '7W-yolov8s', '7W-yolov8n'], 
            mean_list,    
            color=['red', 'blue', 'green', 'purple','yellow', 'orange'], width=0.5)
    
    plt.title('Consumo Medio en C++ (cpugpu)' )
    plt.xlabel('Red y Modo Usados')
    plt.ylabel('Consumo (mW)')
    
    #plt.legend()
    plt.savefig('cppCpuGpuBarras.png')
    #plt.show()
    plt.clf()

def graficar_python_barras():

    plt.figure(figsize=(12, 6)) 
    plt.ylim(1500, 2300)
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
    
    plt.title('Consumo Medio en Python' )
    plt.xlabel('Red y Lenguaje Usados')
    plt.ylabel('Consumo (mW)')
    
    plt.legend()
    plt.savefig('pythonBarras.png')
    #plt.show()
    plt.clf()
    
def leer_datos(ruta):
    f = open(ruta, "r")

    text = f.read()

    powerList = []
    cpugpuList = []

    lines = text.split('\n')

    for line in lines[:-1]:
        line = line.split(' ')

        powerValue = line[-5].split('/')[0][:-2]
        cpugpuValue = line[-3].split('/')[0][:-2]

        #print(cpugpuValue)

        powerList.append(float(powerValue))
        cpugpuList.append(float(cpugpuValue))

    f.close()

    maxV = max(powerList)
    minV = min(powerList)
    meanV = sum(powerList) / len(powerList) 

    print("VinMax: ", maxV)
    print("VinMin: ", minV)
    print("VinMean: ",meanV)
    print("-------------------------")

    maxVcg = max(cpugpuList)
    minVcg = min(cpugpuList)
    meanVcg = sum(cpugpuList) / len(cpugpuList)

    print("VcpugpuMax: ", maxVcg)
    print("VcpugpuMin: ", minVcg)
    print("VcpugpuMean: ",meanVcg) 
    print("-------------------------")

    #graficar_lista(powerList)
    if 'Python' in ruta:
        if '15' in ruta:
            if('yolov8m' in ruta):
                allValues[0][0][0] = powerList
                cpugpuValues[0][0][0] = cpugpuList
            elif('yolov8n' in ruta):
                allValues[0][0][1] = powerList
                cpugpuValues[0][0][1] = cpugpuList
            elif('yolov8s' in ruta):
                allValues[0][0][2] = powerList
                cpugpuValues[0][0][2] = cpugpuList
        elif '7' in ruta:
            if('yolov8m' in ruta):
                allValues[0][1][0] = powerList
                cpugpuValues[0][1][0] = cpugpuList
            elif('yolov8n' in ruta):
                allValues[0][1][1] = powerList
                cpugpuValues[0][1][1] = cpugpuList
            elif('yolov8s' in ruta):
                allValues[0][1][2] = powerList
                cpugpuValues[0][1][2] = cpugpuList
    elif 'c++' in ruta:
        if '15' in ruta:
            if('yolov8m' in ruta):
                allValues[1][0][0] = powerList
                cpugpuValues[1][0][0] = cpugpuList
            elif('yolov8n' in ruta):
                allValues[1][0][1] = powerList
                cpugpuValues[1][0][1] = cpugpuList
            elif('yolov8s' in ruta):
                allValues[1][0][2] = powerList
                cpugpuValues[1][0][2] = cpugpuList
        elif '7' in ruta:
            if('yolov8m' in ruta):
                allValues[1][1][0] = powerList
                cpugpuValues[1][1][0] = cpugpuList
            elif('yolov8n' in ruta):
                allValues[1][1][1] = powerList
                cpugpuValues[1][1][1] = cpugpuList
            elif('yolov8s' in ruta):
                allValues[1][1][2] = powerList
                cpugpuValues[1][1][2] = cpugpuList

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
                #ruta_list = ruta.split('/')

                #model = ruta_list[2].split('.')[0]
                #watios = ruta_list[1]
                if 'best' in ruta :
                    leer_datos(ruta)

# Ejemplo de uso
ruta_carpeta = './scriptResult/'
listar_archivos_y_subcarpetas(ruta_carpeta)

graficar_todos()