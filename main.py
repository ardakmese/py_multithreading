# Operating Systems Homework
# Date: 24.03.2022

import random
import os
import time

class Matrix:
    def __init__(self, x, y):
        self.mX = x
        self.mY = y
        self.mList = {}
        self.fill()

    def fill(self):
        for x in range(len(self.mX)):
            list = {}
            for y  in range(len(self.mY)):
                list.append(range.uniform(0,1))
            self.mList.append(list)
        print(self.mList)

# input two matrices of size n x m
start_time = time.time()
matrix1 = [[12, 7, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[5, 8, 1],
           [6, 7, 3],
           [4, 5, 9]]

res = [[0 for x in range(3)] for y in range(3)]

def multiply():
    # explicit for loops
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                # resulted matrix
                res[i][j] += matrix1[i][k] * matrix2[k][j]


multiply()
print("--- %s seconds ---" % (time.time() - start_time))
print(res)

if __name__ == '__main__':
    while True:
        firstX = input("Please enter first")
        firstMatrix = Matrix(4,5)
