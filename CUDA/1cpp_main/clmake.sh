cl -c -I. main.cpp -o main.cpp.o
nvcc -c -I. GpuSolver.cu -o GpuSolver.cu.o
cl -o exec GpuSolver.cu.o main.cpp.o -lcudart
