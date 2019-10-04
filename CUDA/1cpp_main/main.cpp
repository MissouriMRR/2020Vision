#include <iostream>
#include "GpuSolver.h"

int main()
{
        GpuInterface obj;

        obj.setY(16);

        std::cout << obj.calculateSum() << std::endl;

        return 0;
} 
