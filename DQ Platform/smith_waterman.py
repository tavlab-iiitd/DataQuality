import numpy as np
class smith_waterman(object):
    def __init__(self,string1,string2, match=None, mismatch=None, gap=None):
        self.q = string1
        self.p = string2
        self.gapPen = int(gap)
        self.mismatchPen = int(mismatch)
        self.matchScore = int(match)
        self.finalQ = ""
        self.finalP = ""
        self.MatrixA = np.empty(shape=[len(self.p)+1,len(self.q)+1])
        self.MatrixB = np.empty(shape=[len(self.p)+1,len(self.q)+1])
        self.maxScore = 0
        self.maxI = None
        self.maxJ =None

    def calcTables(self):
        try:
            self.q = '-' + self.q
        except IOError:
            print("Error with sequence 1")

        try:
            self.p = '-' + self.p
        except IOError:
            print("Error with sequence 2")

        self.MatrixA[:,0] = 0
        self.MatrixA[0,:] = 0
        self.MatrixB[:,0] = 0
        self.MatrixB[0,:] = 0

        for i in range(1,len(self.p)):
            for j in range(1, len(self.q)):

                if self.p[i] == self.q[j]:
                    self.MatrixA[i][j] = self.MatrixA[i-1][j-1] + self.matchScore
                    self.MatrixB[i][j] = 3

                    if self.MatrixA[i][j] > self.maxScore:
                        self.maxScore = self.MatrixA[i][j]
                        self.maxI = i
                        self.maxJ = j

                else:
                    self.MatrixA[i][j] = self.findMaxScore(i,j)

    def findMaxScore(self, i, j):

        
        qDelet = self.MatrixA[i-1][j] + self.gapPen
        pDelet = self.MatrixA[i][j-1] + self.gapPen
        mismatch = self.MatrixA[i-1][j-1] + self.mismatchPen
        maxScore = max(qDelet, pDelet, mismatch)

        if qDelet == maxScore:
            self.MatrixB[i][j] = 2 

        elif pDelet == maxScore:
            self.MatrixB[i][j] = 1 

        elif mismatch == maxScore:
            self.MatrixB[i][j] = 3

        return maxScore