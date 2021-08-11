from remove import remove
from Builder1 import matrix_1
from reader import get_data

matrix, time, currents, components = get_data()

for i in range(0, components):
    if(matrix[i][0]==1):
        comp_1 = matrix_1(matrix[i])


