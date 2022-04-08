# Operating Systems Homework
# Date: 07.04.2022
# Author : Arda AKMEŞE

import threading
import time
import random

global sharedData
sharedData = 1000

class ReaderWriter():

    def __init__(self, writerNo = None, writerFunction = None ):
        self.readMutex = threading.Semaphore()
        self.writeMutex = threading.Semaphore()
        self.readerCount = 0
        self.mWriter = writerNo
        self.mFunction = writerFunction


    def reader(self):
        while True:
            self.readMutex.acquire()
            self.readerCount += 1
            global sharedData
            if self.readerCount == 1:
                self.writeMutex.acquire()
            self.readMutex.release()
            print(r"[Okuyucu process", self.readerCount, r"] : Mevcut bakiye=", sharedData)
            self.readMutex.acquire()
            self.readerCount -= 1
            if self.readerCount == 0:
                self.writeMutex.release()
            self.readMutex.release()
            time.sleep(random.randint(1, 5))

    def writer(self):
        while True:
            global sharedData
            self.writeMutex.acquire()
            print(r"[Yazıcı process ", self.mWriter, r"] Mevcut bakiye=",sharedData, end="")
            sharedData = self.mFunction(sharedData)
            print(" Yeni bakiye=", sharedData)
            self.writeMutex.release()
            time.sleep(random.randint(1, 5))


def askForReader():
    print("Lütfen kullanmak istediğiniz Reader sayısını giriniz : ")
    readerSize = input()
    if not readerSize.isdigit() or int(readerSize) < 0:
        print("Lütfen doğru giriniz!")
        askForReader()

    return int(readerSize)

if __name__ == "__main__":
    readerSize = askForReader()

    lambdaIncrease = lambda x: x + 50
    lambdaDivide = lambda x: x - (10 * x / 100)

    writer1 = ReaderWriter(1, lambdaIncrease)
    writer2 = ReaderWriter(2, lambdaDivide)
    thWriter1 = threading.Thread(target=writer1.writer)
    thWriter2 = threading.Thread(target=writer2.writer)
    thWriter1.start()
    thWriter2.start()


    for read in range(readerSize):
            reader = ReaderWriter()
            th = threading.Thread(target=reader.reader)
            th.start()



    # thWriter1.join()
    # thWriter2.join()


