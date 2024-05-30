#!/bin/bash
sudo timeout 60 tegrastats --interval 1 &> scriptResult/Python15w/yolov8nidle.txt &
PID1=$!
timeout 150 /bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8n.engine &
wait $PID1
sudo timeout 60 tegrastats --interval 1 &> scriptResult/Python15w/yolov8nnoidle.txt

sudo timeout 60 tegrastats --interval 1 &> scriptResult/Python15w/yolov8sidle.txt &
PID2=$!
timeout 150 /bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8s.engine &
wait $PID2
sudo timeout 60 tegrastats --interval 1 &> scriptResult/Python15w/yolov8snoidle.txt 

sudo timeout 60 tegrastats --interval 1 &> scriptResult/Python15w/yolov8midle.txt &
PID3=$!
timeout 150 /bin/python3 "/home/nano/Downloads/zed-sdk-master/object detection/custom detector/python/pytorch_yolov8/detector.py" --weights /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/python/pytorch_yolov8/yolov8m.engine &
wait $PID3
sudo timeout 60 tegrastats --interval 1 &> scriptResult/Python15w/yolov8mnoidle.txt 

sudo timeout 60 tegrastats --interval 1 &> scriptResult/c15w/yolov8nidle.txt &
PID4=$!
timeout 150  /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8n.engine 0 &
wait $PID4
sudo timeout 60 tegrastats --interval 1 &> scriptResult/c15w/yolov8nnoidle.txt

sudo timeout 60 tegrastats --interval 1 &> scriptResult/c15w/yolov8sidle.txt &
PID5=$!
timeout 150  /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8s.engine 0 &
wait $PID5
sudo timeout 60 tegrastats --interval 1 &> scriptResult/c15w/yolov8snoidle.txt

sudo timeout 60 tegrastats --interval 1 &> scriptResult/c15w/yolov8midle.txt &
PID6=$!
timeout 150  /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolo_onnx_zed /home/nano/Downloads/zed-sdk-master/object\ detection/custom\ detector/cpp/tensorrt_yolov5-v6-v8_onnx/build/yolov8m.engine 0 &
wait $PID6
sudo timeout 60 tegrastats --interval 1 &> scriptResult/c15w/yolov8mnoidle.txt