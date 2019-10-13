g++ -c -I. main.cpp -o main.cpp.o
nvcc -c -I. -I/usr/local/cuda/include GpuSolver.cu -o GpuSolver.cu.o
g++ -o exec GpuSolver.cu.o main.cpp.o -L/usr/local/cuda/lib -lcudart
