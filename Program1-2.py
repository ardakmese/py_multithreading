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
    firstX = input("Lütfen ilk matrisin sütun sayısını giriniz: ")
    firstY = input("Lütfen ilk matrisin satır sayısını giriniz: ")
    secondX = input("Lütfen ikinci matrisin sütun sayısını giriniz: ")
    secondY = input("Lütfen ikinci matrisin satır sayısını giriniz: ")

    if not (firstX.isdigit() or firstY.isdigit() or secondX.isdigit() or secondY.isdigit()):
        print("Lütfen doğru giriniz!")
        setMatrix()
    elif not (firstX == secondX and firstY == secondY) and  (firstY != secondX ):  #iki matrisin çarpılması için gerekli kontrol
        print("Lütfen çarpım için boyutları doğru giriniz!")
        setMatrix()

def multiplyWithThreading():
    # setMatrix()
    threadSize = input("Lütfen matrislerin çarpımında kullanılacak thread sayısını giriniz : ")
    if not threadSize.isdigit():
        print("Girilen thread sayısı doğru değil!")
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

    print( threadSize + " thread ile hesaplanan çarpım süresi: ", (time.time() - start_time), " saniye")
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

        print("Tek thread ile hesaplanan süre:", oneThreadTime,
              "saniye, multithreading ile yapılan çarpımda hesaplanan süre:", multiThreadTime, " saniye")

