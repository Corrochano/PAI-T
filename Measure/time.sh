#!/bin/bash

timeout 300 /bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8n.engine &> scriptResult/Python7w/timeyolov8n.txt

timeout 300 /bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8m.engine &> scriptResult/Python7w/timeyolov8m.txt

timeout 300 /bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8s.engine &> scriptResult/Python7w/timeyolov8s.txt

timeout 300 /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8n.engine 0 &> scriptResult/c++7w/timeyolov8n.txt

timeout 300 /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8m.engine 0 &> scriptResult/c++7w/timeyolov8m.txt

timeout 300 /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8s.engine 0 &> scriptResult/c++7w/timeyolov8s.txt
