import time
import numpy
class Solution :
    N, p, s, grid, scooterPositions, score, police, activityScore = 0, 0, 0, [], [], 0, 0, []
    matrix = []
    count = 0
    def __init__(self, inputFile, outputFile):
        start_time = time.time()
        scooterPositions = []
        file = open(inputFile, "r")
        f = file.readlines()
        self.N = int(f.__getitem__(0))
        self.p = int(f.__getitem__(1))
        self.s = int(f.__getitem__(2))
        # self.N = 4
        # self.p = 2
        # self.s = int(f.__getitem__(2))
        print("grid length", self.N)
        print("Police count ", self.p)
        print("Scooter count", self.s)
        l=[]
        # print(f.__len__())
        for i in range(3, f.__len__()):
            if i > 3 and (i - 3) % self.s == 0:
                self.scooterPositions.append(l)
                l = []
            temp = []
            obj = f.__getitem__(i).strip().split(",")
            temp.append(obj[0])
            temp.append(obj[1])
            l.append(temp)
        self.scooterPositions.append(l)
        self.activityScore = [[0 for y in range(self.N)] for x in range(self.N)]
        # print(self.activityScore)
        # self.populateActivityScore()
        self.activityScore = [[47, 44, 15, 45, 48, 49, 39, 2, 4, 13, 10, 37, 2, 42, 3], [32, 13, 17, 13, 23, 16, 40, 6, 41, 8, 31, 15, 33, 39, 19], [10, 22, 29, 29, 49, 6, 16, 48, 32, 3, 6, 16, 22, 3, 1], [41, 24, 49, 40, 45, 35, 36, 45, 1, 33, 14, 28, 43, 23, 27], [37, 45, 9, 25, 36, 28, 23, 43, 19, 9, 14, 26, 9, 44, 40], [27, 36, 25, 21, 16, 17, 50, 6, 47, 49, 4, 10, 27, 29, 19], [29, 32, 29, 37, 49, 27, 31, 44, 8, 29, 28, 30, 36, 15, 0], [5, 24, 30, 38, 13, 19, 19, 28, 47, 42, 20, 32, 25, 15, 47], [1, 25, 11, 19, 7, 45, 41, 12, 10, 14, 2, 46, 0, 44, 30], [40, 44, 5, 46, 33, 10, 30, 47, 33, 17, 49, 41, 28, 41, 23], [50, 49, 16, 25, 8, 40, 8, 6, 49, 25, 22, 44, 23, 40, 48], [7, 30, 31, 36, 16, 43, 8, 2, 44, 0, 44, 32, 21, 16, 19], [24, 23, 5, 34, 49, 4, 5, 5, 2, 48, 3, 44, 27, 29, 3], [41, 13, 27, 33, 11, 3, 30, 49, 36, 10, 45, 27, 2, 44, 23], [32, 35, 27, 23, 43, 38, 12, 45, 0, 13, 13, 32, 27, 3, 13]]





        # self.printBoard(self.activityScore)
        file.close()
        # print(self.scooterPositions.__len__())
        self.grid = [[0 for x in range(self.N)] for y in range(self.N)]
        self.police = self.p
        result = 0
        self.arrangePolice(0, self.p, 0, 0)
        # print("DONE!!!")
        print("--- %s seconds ---" % (time.time() - start_time))
        print(self.police, "is the police")
        print(self.count, "is the count")
        # print(self.matrix)
        # for pol in self.matrix:
        #     # print(self.s)
        #     temp = self.countActivityPoints(pol, self.s)
        #     # print(temp, "is the temporary score")
        #     if temp > self.score:
        #         self.score = temp
        print(self.score, "is the score")
        file = open(outputFile, "w+")
        file.write(str(self.score))
        file.close()
    def populateActivityScore(self):
        s = self.s
        for time in self.scooterPositions:
            t = 0
            while t < s:
                self.activityScore[int(time[t][0])][int(time[t][1])] += 1
                t = t + 1
    def arrangePolice(self, col, p, result, result_t):
        # write algorithm for arranging p police in grid and iterate over each such possible grid
        # for each arrangement call countActivityPoints method
        if p == 0:
            # if self.police == self.numberOfOnes():
                # print(self.grid)
                # print(l)
            # self.printBoard(self.grid)
            if(self.score < max([result_t, result])):
                self.score = max([result_t, result])
            # print(self.score)
            # temp = self.countActivityPoints(self.grid, self.s)
            # if temp > self.score:
            #     self.score = temp
            self.count = self.count + 1
            return
        for j in range(col, self.N):

            for i in range(0, self.N):
                if p == self.police:
                    if i > int(self.N/2) + 1:
                        continue
                # print(j, i)
                # s = calculateMaxScoreSum(col)
                if self.isSafe(j, i) and self.N-j >= p:
                    self.grid[i][j] = 1
                    result += self.activityScore[i][j]
                    result_t += self.activityScore[j][i]
                    p = p - 1
                    self.arrangePolice(j + 1, p, result, result_t)
                    self.grid[i][j] = 0
                    p = p + 1
                    result -= self.activityScore[i][j]
                    result_t -= self.activityScore[j][i]

    # def numberOfOnes(self):
    #     c = 0
    #     for i in range(0, self.N):
    #         for j in range(0, self.N):
    #             if self.grid[i][j] == 1:
    #                 c = c + 1
    #     return c

    # def calculateMaxScoreSum(self, col):
    #     s = 0
    #     for i in range(col, self.N):
    #         s += max(self.grid[i])
    #     return s

    def isSafe(self, col, row):
        for i in range(0, col):
            if self.grid[row][i] == 1:
                return False
        i = row
        j = col
        while i>=0 and j>=0:
            if self.grid[i][j] == 1:
                return False
            i = i - 1
            j = j - 1

        i = row
        j = col
        while i < self.N and j >= 0:
            if self.grid[i][j] == 1:
                return False
            i = i + 1
            j = j - 1
        return True

    def printBoard(self, grid):
        for i in range(0, self.N):
            for j in range(0, self.N):
                print(grid[i][j], "", end=" ")
            print("")
        print("")

    def countActivityPoints(self, pol, s):
        trans = numpy.transpose(pol)
        # self.printBoard(pol)
        # self.printBoard(trans)
        t = 0
        score = 0
        score2 = 0
        self.activityScore=[[24, 41, 30, 25, 41, 4, 22, 35, 40, 43], [22, 8, 7, 6, 27, 30, 50, 29, 38, 44], [45, 33, 17, 43, 42, 8, 16, 17, 24, 41], [10, 44, 8, 46, 6, 1, 1, 44, 6, 49], [39, 10, 2, 41, 17, 27, 15, 15, 17, 39], [31, 31, 42, 30, 42, 21, 27, 12, 1, 8], [31, 19, 26, 11, 35, 28, 16, 34, 37, 31], [0, 20, 33, 35, 12, 50, 5, 18, 29, 15], [22, 15, 21, 42, 48, 26, 37, 17, 10, 43], [24, 48, 5, 24, 35, 26, 5, 7, 25, 39]]


        # print(self.scooterPositions)


        # self.printBoard(self.scooterPositions)
        # for time in self.scooterPositions:
        #     t = 0
        #     while t < s:
        #         if pol[int(time[t][0])][int(time[t][1])] == 1:
        #             score = score + 1
        #         if trans[int(time[t][0])][int(time[t][1])] == 1:
        #             score2 = score2 + 1
        #         t = t + 1

        for i in range(0,self.N):
            for j in range(0, self.N):
                if pol[i][j] == 1:
                    score += self.activityScore[i][j]
                if trans[i][j] == 1:
                    score2 += self.activityScore[i][j]
        if score2 > score:
            return score2
        else:
            return score

sol = Solution("input3.txt", "output.txt")
