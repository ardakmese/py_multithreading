# Operating Systems Homework
# Date: 24.03.2022

import random
import os
import time
import threading as thread

class Matrix:
    def __init__(self, x, y, threading = 0):
        self.mX = x
        self.mY = y
        self.mList = []
        self.fill()
        self.mThread = threading

    def fill(self):
        for x in range(self.mX):
            list = []
            for y  in range(self.mY):
                list.append(random.uniform(0,1))
            self.mList.append(list)
        print("Matrix to multiply: ", self.mList)

    def multiply(self, matrix):
        start_time = time.time()
        res = [[0 for x in range(self.mX)] for y in range(matrix.mY)]
        for i in range(self.mX):
            for j in range(matrix.mY):
                for k in range(matrix.mX):
                    res[i][j] += self.mList[i][k] * matrix.mList[k][j]
        print("Result ", res)
        print("--- %s seconds ---" % (time.time() - start_time))

    def multiplyWithThread(self, matrix):
        start_time = time.time()
        res = [[0 for x in range(self.mX)] for y in range(matrix.mY)]

        for i in range(self.mX):
            for j in range(matrix.mY):
                for k in range(matrix.mX):
                    res[i][j] += self.mList[i][k] * matrix.mList[k][j]


        print("Result ", res)
        print("--- %s seconds ---" % (time.time() - start_time))


# input two matrices of size n x m
# res = [[0 for x in range(3)] for y in range(3)]

def setMatrix():
    global firstX, firstY, secondX, secondY
    global firstMatrix, secondMatrix
    firstX = input("Please enter first matrix's column size: ")
    firstY = input("Please enter first matrix's row size: ")
    secondX = input("Please enter second matrix's column size: ")
    secondY = input("Please enter second matrix's row size: ")

    if not (firstX.isdigit() or firstY.isdigit() or secondX.isdigit() or secondY.isdigit()):
        print("Please enter inputs correctly!")
        setMatrix()
    elif not (firstX == secondX and firstY == secondY) and  (firstY != secondX ):  # necessary for multiplying two matrixes to check dimensions!
        print("Please enter dimensions correctly for multiplying!")
        setMatrix()

def multiplyWithThreading():
    setMatrix()
    threadSize = input("Please enter thread size to use while multiplying: ")
    if not threadSize.isdigit():
        print("Input is not correct!")
        multiplyWithThreading()

    firstMatrix = Matrix(int(firstX), int(firstY), int(threadSize))
    secondMatrix = Matrix(int(secondX), int(secondY))

    thread_handle = []
    for j in range(0, int(threadSize)):
        t = thread(target=firstMatrix.multiply, args= secondMatrix)
        thread_handle.append(t)
        t.start()

    for j in range(0, int(threadSize)):
        thread_handle[j].join()

if __name__ == '__main__':
    while True:
        # multiply with one thread
        # setMatrix()
        # firstMatrix = Matrix(int(firstX), int(firstY))
        # secondMatrix = Matrix(int(secondX), int(secondY))
        # firstMatrix.multiply(secondMatrix)
        # multiply with multithreading

        start_time = time.time()
        multiplyWithThreading()
        print("--- %s seconds ---" % (time.time() - start_time))


