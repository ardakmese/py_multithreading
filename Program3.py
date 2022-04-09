# Operating Systems Homework
# Date: 07.04.2022
# Author : Arda AKMEŞE

import threading
import time
import random

global sharedData
sharedData = 1000

readMutex = threading.Semaphore()
writeMutex = threading.Semaphore()


class Reader():
    def __init__(self):
        self.readCount = 0
        self.readerCalledCounter = 0

    def reader(self):
        while True:
            readMutex.acquire()
            self.readCount += 1
            global sharedData
            if self.readCount == 1:
                writeMutex.acquire()
            readMutex.release()
            self.readerCalledCounter += 1
            print(r"[Okuyucu process", self.readCount, r"] : Mevcut bakiye=", sharedData)
            print("Toplam okuma sayısı:", self.readerCalledCounter)
            readMutex.acquire()
            self.readCount -= 1
            if self.readCount == 0:
                writeMutex.release()
            readMutex.release()
            time.sleep(random.randint(0, 5))

class Writer():
    def __init__(self):
        self.writerCalledCounter = 0

    def writer(self):
        while True:
            writeMutex.acquire()
            global sharedData
            print(r"[Yazıcı process 1] Mevcut bakiye=", sharedData, end="")
            sharedData = sharedData + 50
            self.writerCalledCounter += 1
            print(", 50 arttırıldı. Yeni bakiye=", sharedData)
            print("Toplam yazma sayısı:", self.writerCalledCounter)
            writeMutex.release()
            time.sleep(random.randint(0, 5))

    def writer2(self):
        while True:
            writeMutex.acquire()
            global sharedData
            print(r"[Yazıcı process 2] Mevcut bakiye=", sharedData, end="")
            sharedData =  sharedData - (10 * sharedData / 100)
            self.writerCalledCounter += 1
            print(", %10 azaltıldı. Yeni bakiye=", sharedData)
            writeMutex.release()
            time.sleep(random.randint(0, 5))


def askForReader():
    print("Lütfen kullanmak istediğiniz Reader sayısını giriniz : ")
    readerSize = input()
    if not readerSize.isdigit() or int(readerSize) < 0:
        print("Lütfen doğru giriniz!")
        askForReader()

    return int(readerSize)

if __name__ == "__main__":
    readerSize = askForReader()
    reader = Reader()
    for read in range(readerSize):
        th = threading.Thread(target=reader.reader)
        th.start()

    writer = Writer()
    writer1 = threading.Thread(target=writer.writer)
    writer1.start()

    writer2 = threading.Thread(target=writer.writer2)
    writer2.start()
