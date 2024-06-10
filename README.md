# Integración de YOLO en Nvidia Jetson Orin Nano
Este proyecto consiste en la integración de un modelo de detección de objetos en un embalse (barcos, surfistas, etc) en una Nvidida Jetson Orin Nano que lleva una cámara Zed 2i.

## Inicializar la placa
El primer paso para lograr trabjar en la placa es flashearle el SO. Según comenta el fabricante en https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit#intro esto se puede hacer por dos vías.
Nosotros usamos una SD card, en la cual quemamos JetPAck 5.1.3 ya que, aunque ya se disponía de Jetpack 6.0, el mismo fabricante comenta en https://www.jetson-ai-lab.com/initial_setup_jon.html que es necesario flashear la versión 5.1.3 para que se pueda actualizar el firmware.

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
sudo nvpmodel -m 1
```

  Donde 1 es el modo 7W. PAra cambiar a 15W, ejecutamos ese mismo comando pero indicando -m 0.

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
PAra la instalación de tanto Pytorch como torchvision se debe seguir el siguiente tutorial para poder utilizar cuda: https://docs.ultralytics.com/guides/nvidia-jetson/#install-pytorch-and-torchvision

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

Se instaló OpenCV 4.5.4

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

Se ejecutó TrtExec, que se descargó de la siguiente web: https://developer.nvidia.com/tensorrt

Para ejecutarlo, nos vamos a la dirección donde lo hayamos instalado (ennuestro caso, /usr/src/tensorrt/bin/):

```
cd /usr/src/tensorrt/bin/
```

Y una vez allí, ejecutamos el modelo deseado con el flag --loadEngine. 

Por ejemplo, si queremos ejecutar el modelo yolov8n.engine que tenemos en /home/nano/cppFolder/build/ haríamos lo siguiente:

```
./trtexec /home/nano/cppFolder/build/yolov8n.engine
```
