# Operating Systems Homework
# Date: 24.03.2022
# Author : Arda AKMEŞE

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
        # print("Matrix to multiply: ", self.mList)

    def multiply(self, matrix):
        start_time = time.time()
        res = [[0 for x in range(self.mX)] for y in range(matrix.mY)]
        for i in range(self.mX):
            for j in range(matrix.mY):
                for k in range(matrix.mX):
                    res[i][j] += self.mList[i][k] * matrix.mList[k][j]
        # print("Çarpım sonucu : ", res)
        print("Tek thread ile çarpımda geçen süre : ", (time.time() - start_time), " saniye")
        return time.time() - start_time

    def multiplyWithThread(self, matrix, vecStart, vecEnd):
        res = [[0 for x in range(self.mX)] for y in range(matrix.mY)]
        for i in range(vecStart, vecEnd):
            for j in range(matrix.mY):
                for k in range(matrix.mX):
                    res[i][j] += self.mList[i][k] * matrix.mList[k][j]
