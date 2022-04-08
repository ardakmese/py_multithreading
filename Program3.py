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

    def reader(self):
        while True:
            readMutex.acquire()
            self.readCount += 1
            global sharedData

            if self.readCount == 1:
                writeMutex.acquire()
            readMutex.release()
            print(f"Reader {self.readCount} is reading as: ", sharedData)
            readMutex.acquire()
            self.readCount -= 1
            if self.readCount == 0:
                writeMutex.release()
            readMutex.release()
            time.sleep(random.randint(1 ,5))

class Writer():
    def __init__(self, writerNo):
        self.mWriter = writerNo

    def writer(self):
        while True:
            writeMutex.acquire()  # wait on write semaphore
            global sharedData
            print("Wrting data.....")  # write the data
            sharedData += 50
            sharedData -= 10 * sharedData / 100
            print("data ", sharedData)
            writeMutex.release()  # sinal on write semaphore
            time.sleep(random.randint(1 ,5))



def askForReader():
    print("Please enter how many reader you would like to use in the project: ")
    readerSize = input()
    if not readerSize.isdigit() or readerSize < 0:
        print("Please enter correctly!")
        askForReader()

    return int(readerSize)

if __name__ == "__main__":
    readerSize = askForReader()
    readerThList = []
    for read in range(readerSize):
            reader = Reader()
            th = threading.Thread(target=reader.reader())
            th.start()
            th.join()

