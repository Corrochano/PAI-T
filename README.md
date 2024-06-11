# Integración de YOLO en Nvidia Jetson Orin Nano
Este proyecto consiste en la integración de un modelo de detección de objetos en un embalse (barcos, surfistas, etc) en una Nvidida Jetson Orin Nano que lleva una cámara Zed 2i.

## Autores
Este repositorio ha sido creado por Álvaro Corrochano López y Iulius Gherasim.

## Inicializar la placa
El primer paso para lograr trabjar en la placa es flashearle el SO. Según comenta el fabricante en https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit#intro esto se puede hacer por dos vías.
Nosotros usamos una SD card, en la cual quemamos JetPack 5.1.3 ya que, aunque ya se disponía de Jetpack 6.0, el mismo fabricante comenta en https://www.jetson-ai-lab.com/initial_setup_jon.html que es necesario flashear la versión 5.1.3 para que se pueda actualizar el firmware.

## Cambiar modo de energía
LA Nvidia Jetson Orin NAno permite operart en dos modos de energía distintos: 7W y 15W.

Si queremos comprobar en que modo estamos, esto lo podemos comprobar en la parte superior derecha, lugar donde también podemos cambiar el modo.

Si queremos hacer la comprobación por línea de comandos, ejecutamos el siguiente comando:

```
sudo nvpmodel -q
```

O este otro, el cual mira el directorio por defecto donde se encuentran estos modos configurados:
```
sudo /usr/sbin/nvpmodel -q
```

Para cambiar de modo ejecutamos el siguiente comando:
```
sudo nvpmodel -m x
```

Donde 1 es el modo 7W y 0 el modo 15W.

## Repositorio de GitLab con los modelos
Se han probado los modelos realizados por José Luís Mela Navarro, que se encuentran en el siguiente enlace: https://gitlab.com/Ljmn30/tfm

## Instalación de la librería zedsl
Para utilizar la cámara ZED 2i se debe instalar primero el sdk en el siguiente enlace: https://www.stereolabs.com/developers/release
En concreto, gemos instalado la versión ZED SDK for JetPack 5.1.2 (L4T 35.4) 4.1 (Jetson Xavier, Orin AGX/NX/Nano, CUDA 11.4)
Para ello se puede seguir la siguiente guía: https://www.stereolabs.com/docs/installation/jetson

Tras esto, se debe ejecutar un script proporcionado en la instalación para instalar pyzed. Por defecto se encuentra en "/usr/local/zed/" 
Una vez en el directorio, ejecutamos "python3 get_python_api.py"

Para ello, se puede seguir el siguiente tutorial: https://www.stereolabs.com/docs/app-development/python/install

## Instalación de PyTorch
Para la instalación de tanto Pytorch como torchvision se debe seguir el siguiente tutorial para poder utilizar cuda: https://docs.ultralytics.com/guides/nvidia-jetson/#install-pytorch-and-torchvision

En el mismo, se especifica que se debe descargar una versión de pytorch específica para la placa y clonar un repositorio con el que se buildea la versión especifica de torchvision.

```
sudo apt-get install -y libopenblas-base libopenmpi-dev
wget https://developer.download.nvidia.com/compute/redist/jp/v512/pytorch/torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl -O torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl
pip install torch-2.1.0a0+41361538.nv23.06-cp38-cp38-linux_aarch64.whl
```

```
sudo apt install -y libjpeg-dev zlib1g-dev
git clone https://github.com/pytorch/vision torchvision
cd torchvision
git checkout v0.16.2
python3 setup.py install --user
```

## Cómo activar OpenCV con CUDA
Para activar OpenCV cpn CUDA se usó el siguiente tutorial: https://jetsonhacks.com/2023/11/07/opencv-with-cuda-in-python-on-jetson/

En el mismo, se explica que se debe descargar el repositorio de OpenCV y cambiar el script de instalación a nuestros requisitos específicos.
En nuestro caso, tenemos CUDA 11.8.89 ya que es la versión más reciente que nos permite tener Jestpack 5.1.3 a fecha actual. TAmbién se tiene instalado Python 3.8.10.

Por ello, se instaló OpenCV 4.5.4

Si se necesita otra versión específica, se pueden encontrar todos los whl en el siguiente enlace: https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048
En esa misma página en el apartado de installation, se explica a fondo la instalación de torchvision.

## Conversión a TensorRT

Para la conversión de Pytorch a TensorRT de los modelos, se siguió su apartado en el siguiente tutorial: https://docs.ultralytics.com/guides/nvidia-jetson/#install-onnxruntime-gpu

``` Python
from ultralytics import YOLO

# Load a YOLOv8n PyTorch model
model = YOLO("yolov8n.pt")

# Export the model
model.export(format="engine")  # creates 'yolov8n.engine'

# Load the exported TensorRT model
trt_model = YOLO("yolov8n.engine")

# Run inference
results = trt_model("https://ultralytics.com/images/bus.jpg")
```

## Versión C++
Para que un modelo se ejecute correctamente en C++ hay primero que pasarlo a TensorRT mediante el mismo programa de la siguiente manera:

```
./yolo_onnx_zed -s tuArchivo.onnx nombreDeseado.engine
```

Luego para ejecutar usamos el siguente comando:

```
./yolo_onnx_zed tuArchivo.engine 0
```

Para ejcutar con vídeo, ejecutamos el siguiente comando:

```
./yolo_onnx_zed tuArchivo.engine tuArchivo.svo
```
## TrtExec

Se ejecutó TrtExec para medir los ms de inferencia y también para crear un archivo engine lo más eficiente posible.
TrtExec se descargó de la siguiente web: https://developer.nvidia.com/tensorrt

Para ejecutarlo, nos vamos a la dirección donde lo hayamos instalado (la ruta por defecto es /usr/src/tensorrt/bin/):

```
cd /usr/src/tensorrt/bin/
```

Y una vez allí, ejecutamos el modelo deseado con el flag --loadEngine. 

```
./trtexec --loadEngine=tuModelo.engine
```
Se crearon archivos .engine con el flag best, que cuantiza los pesos de la forma más eficiente. 
El comando utilizado fue:
```
./trtexec --onnx=tuArchivo.onnx --saveEngine=comoLoQuierasGuardar.engine --best
```
## Tegrastats
Tegrastats es una herramienta que nos permite visualizar el consumo energético de la placa.
Se debe lanzar con sudo para que muestre todos los detalles:

```
sudo tegrastats
```
Adicionalmente, se puede indicar que mida los datos cada x milisegundos que queramos de la siguiente forma:
```
sudo tegrastats --interval x
```

Tegrastats, entre otras cosas, da tres valores de energía en la Jetson Orin nano: 
- VDD_IN: Consumo total
- VDD_CPU_GPU_CV: Consumo de la cpu y de la gpu
- VDD_SOC: Consumo de otros componentes empotrados

Los tres campos tienen el valor puntual a la izquierda y la media de lo que se lleva ejecutando a la derecha de la forma xxxxmW/yyyymW.

Se puede consultar más informacion sobre tegrastats en https://docs.nvidia.com/drive/drive_os_5.1.6.1L/nvvib_docs/index.html#page/DRIVE_OS_Linux_SDK_Development_Guide/Utilities/util_tegrastats.html#
ó en https://docs.nvidia.com/jetson/archives/r34.1/DeveloperGuide/text/AT/JetsonLinuxDevelopmentTools/TegrastatsUtility.html#reported-statistics

