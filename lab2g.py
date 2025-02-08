#!/usr/bin/env python3
# Author: Biswas Turja Nandini Dia
# Author ID: 119673226
# Date Created: 2024/09/29


import sys  

timer = 3  


if len(sys.argv) > 1:
    timer = int(sys.argv[1])  


while timer > 0:
    print(timer)  
    timer -= 1    


print('blast off!')
