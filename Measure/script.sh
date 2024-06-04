#!/bin/bash

sudo timeout 300 tegrastats --interval 1000 &> scriptResult/Python15w/yolov8nidle.txt &
PID1=$!
/bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8n.engine &
PYTHON_PID1=$!
wait $PID1
sudo timeout 300 tegrastats --interval 1000 &> scriptResult/Python15w/yolov8nnoidle.txt
sleep 630 
kill -9  $PYTHON_PID1 

sudo timeout 300 tegrastats --interval 1000 &> scriptResult/Python15w/yolov8sidle.txt &
PID2=$!
/bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8s.engine &
PYTHON_PID2=$!
wait $PID2
sudo timeout 300 tegrastats --interval 1000 &> scriptResult/Python15w/yolov8snoidle.txt 
sleep 630 
kill -9 $PYTHON_PID2 


sudo timeout 300 tegrastats --interval 1000 &> scriptResult/Python15w/yolov8midle.txt &
PID3=$!
/bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8m.engine &
PYTHON_PID3=$!
wait $PID3
sudo timeout 300 tegrastats --interval 1000 &> scriptResult/Python15w/yolov8mnoidle.txt 
sleep 630 
kill -9  $PYTHON_PID3


sudo timeout 300 tegrastats --interval 1000 &> scriptResult/c15w/yolov8nidle.txt &
PID4=$!
/home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8n.engine 0 &
PYTHON_PID4=$!
wait $PID4
sudo timeout 300 tegrastats --interval 1000 &> scriptResult/c15w/yolov8nnoidle.txt
sleep 630
kill -9  $PYTHON_PID4


sudo timeout 300 tegrastats --interval 1000 &> scriptResult/c15w/yolov8sidle.txt &
PID5=$!
/home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8s.engine 0 &
PYTHON_PID5=$!
wait $PID5
sudo timeout 300 tegrastats --interval 1000 &> scriptResult/c15w/yolov8snoidle.txt
sleep 630
kill -9  $PYTHON_PID5


sudo timeout 300 tegrastats --interval 1000 &> scriptResult/c15w/yolov8midle.txt &
PID6=$!
/home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8m.engine 0 &
PYTHON_PID6=$!
wait $PID6
sudo timeout 300 tegrastats --interval 1000 &> scriptResult/c15w/yolov8mnoidle.txt
sleep 630
kill -9  $PYTHON_PID6


timeout 300 /bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8n.engine &> scriptResult/Python15w/timeyolov8n.txt

timeout 300 /bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8m.engine &> scriptResult/Python15w/timeyolov8m.txt

timeout 300 /bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8s.engine &> scriptResult/Python15w/timeyolov8s.txt

timeout 300 /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8n.engine 0 &> scriptResult/c++15w/timeyolov8n.txt

timeout 300 /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8m.engine 0 &> scriptResult/c++15w/timeyolov8m.txt

timeout 300 /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8s.engine 0 &> scriptResult/c++15w/timeyolov8s.txt




sudo shutdown