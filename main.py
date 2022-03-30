# Operating Systems Homework
# Date: 24.03.2022

import random
import os
import time

class Matrix:
    def __init__(self, x, y):
        self.mX = x
        self.mY = y
        self.mList = []
        self.fill()

    def fill(self):
        for x in range(self.mX):
            list = []
            for y  in range(self.mY):
                list.append(random.uniform(0,1))
            self.mList.append(list)
        print(self.mList)

    def multiply(self,matrix):
        start_time = time.time()
        for i in range(self.mX):
            for j in range(matrix.mY):
                for k in range(matrix.mX):
                    # resulted matrix
                    res[i][j] += matrix1[i][k] * matrix2[k][j]
        print(res)

# input two matrices of size n x m
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

if __name__ == '__main__':
    while True:
        firstX = input("Please enter first matrix's column size: ")
        firstY = input("Please enter first matrix's row size: ")
        secondX = input("Please enter second matrix's column size: ")
        secondY = input("Please enter second matrix's row size: ")

        if not (firstX.isdigit() or firstY.isdigit() or secondX.isdigit() or secondY.isdigit()):
            print("Please enter inputs correctly!")
            continue
        elif not (firstX == secondX and firstY == secondY) or (firstX != secondX and firstX == secondY):  # necessary for multiplying two matrixes to check dimensions!
            print("Please enter dimensions correctly for multiplying!")
            continue

        firstMatrix = Matrix(int(firstX),int(firstY))
        secondMatrix = Matrix(int(secondX),int(secondY))

