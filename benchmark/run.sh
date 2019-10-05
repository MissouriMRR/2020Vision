#!/bin/bash
g++ -std=c++17 -Wall opencv.cpp -lopencv_core -lopencv_highgui -lopencv_imgproc -o opencv.exe
./opencv.exe
