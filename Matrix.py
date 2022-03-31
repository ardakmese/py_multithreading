import random
import time

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
        # print("Multiplied Matrix : ", res)
        print("Time result with one thread %s " % (time.time() - start_time), " seconds")

    def multiplyWithThread(self, matrix, thStart, thEnd):
        res = [[0 for x in range(self.mX)] for y in range(matrix.mY)]
        for i in range(thStart, thEnd):
            for j in range(matrix.mY):
                for k in range(matrix.mX):
                    res[i][j] += self.mList[i][k] * matrix.mList[k][j]