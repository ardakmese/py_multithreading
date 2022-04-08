# Operating Systems Homework
# Date: 24.03.2022
# Author : Arda AKMEŞE

import os
import time
from threading import Thread
from Matrix import Matrix

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
    threadSize = input("Please enter thread size to use for multiplying same matrixes : ")
    if not threadSize.isdigit():
        print("Thread input is not correct!")
        multiplyWithThreading()

    firstMatrix = Matrix(int(firstX), int(firstY), int(threadSize))
    secondMatrix = Matrix(int(secondX), int(secondY))
    mThread = int(threadSize)
    threadList = []

    start_time = time.time()
    for i in range(int(threadSize)):
        thread = Thread(target=firstMatrix.multiplyWithThread,
                   args= (secondMatrix, (int(int(firstX)/mThread) * i), int((int(secondY)/mThread) * (i+1))))
        thread.start()
        threadList.append(thread)

    for i in range(int(threadSize)):
        threadList[i].join()

    print("Calculation time while using " + threadSize + " thread: ", (time.time() - start_time), " seconds")
    return time.time() - start_time


if __name__ == '__main__':
    while True:
        # multiply with one thread
        setMatrix()
        firstMatrix = Matrix(int(firstX), int(firstY))
        secondMatrix = Matrix(int(secondX), int(secondY))
        oneThreadTime = firstMatrix.multiply(secondMatrix)

        # multiply with multithreading
        multiThreadTime = multiplyWithThreading()

        print("First calculation with one thread:", oneThreadTime,
              "seconds, and second calculation with multithreading:", multiThreadTime, " seconds")

