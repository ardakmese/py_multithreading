# Operating Systems Homework
# Date: 24.03.2022

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
    threadSize = input("Please enter thread size to use while multiplying: ")
    if not threadSize.isdigit():
        print("Input is not correct!")
        multiplyWithThreading()

    firstMatrix = Matrix(int(firstX), int(firstY), int(threadSize))
    secondMatrix = Matrix(int(secondX), int(secondY))
    mThread = int(threadSize)
    thread_handle = []

    start_time = time.time()
    for j in range(0, int(threadSize)):
        t = Thread(target=firstMatrix.multiplyWithThread,
                   args= (secondMatrix, (int(int(firstX)/mThread) * j), int((int(secondY)/mThread) * (j+1))))
        thread_handle.append(t)
        t.start()
    for j in range(0, int(threadSize)):
        thread_handle[j].join()

    print("Time result while using " + threadSize + " thread: ", (time.time() - start_time) , " seconds")


if __name__ == '__main__':
    while True:
        # multiply with one thread
        setMatrix()
        firstMatrix = Matrix(int(firstX), int(firstY))
        secondMatrix = Matrix(int(secondX), int(secondY))
        firstMatrix.multiply(secondMatrix)

        # multiply with multithreading
        multiplyWithThreading()


