import time
import numpy
from heapq import nlargest
class Solution :
    N, p, s, grid, scooterPositions, score, police, activityScore = 0, 0, 0, [], [], 0, 0, []
    matrix = []
    count = 0

    # Read data from input file and start the recusrion process for placing p policemen in n x n grid
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

        # print("grid length", self.N)
        # print("Police count ", self.p)
        # print("Scooter count", self.s)
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
        self.populateActivityScore()
        # self.activityScore = [[44, 41, 17, 2, 20, 34, 40, 8, 33, 22, 26, 17, 14], [16, 37, 6, 45, 32, 19, 23, 0, 23, 9, 39, 2, 46], [50, 29, 31, 5, 7, 12, 39, 34, 2, 29, 2, 2, 24], [12, 0, 46, 7, 11, 10, 7, 48, 10, 13, 11, 33, 41], [18, 28, 45, 28, 31, 22, 43, 0, 35, 22, 1, 15, 1], [36, 43, 28, 17, 10, 23, 16, 19, 25, 45, 12, 10, 18], [23, 30, 50, 8, 43, 1, 22, 32, 16, 50, 34, 0, 0], [19, 28, 19, 34, 25, 6, 26, 29, 36, 17, 15, 27, 34], [6, 12, 29, 2, 35, 21, 28, 36, 17, 2, 31, 37, 27], [17, 43, 36, 37, 24, 15, 13, 25, 44, 28, 7, 29, 48], [31, 6, 24, 16, 8, 13, 50, 1, 50, 9, 2, 36, 39], [16, 21, 36, 19, 49, 44, 4, 0, 36, 22, 15, 30, 5], [30, 10, 38, 24, 8, 32, 21, 0, 31, 21, 8, 10, 15]]


        # self.printBoard(self.activityScore)

        # self.printBoard(self.activityScore)
        file.close()
        # print(self.scooterPositions.__len__())
        self.grid = [[0 for x in range(self.N)] for y in range(self.N)]
        self.police = self.p
        result = 0
        if (self.N == 14 and self.police == 14 ) or (self.N == 15 and self.police == 15):
            self.nQueens(0, 0)
            file = open(outputFile, "w+")
            print(self.count)
            print(self.score)
            file.write(str(self.score))
            file.close()
            print("--- %s seconds ---" % (time.time() - start_time))
            return
        self.arrangePolice(0, self.p, 0)
        # print("DONE!!!")
        print("--- %s seconds ---" % (time.time() - start_time))
        # print(self.police, "is the police")
        # print(self.count, "is the count")
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

    # Basic nQueens problem
    def nQueens(self, col, result):
        if col == self.N:
            # self.printBoard(self.grid)

            if result > self.score:
                self.score = result
            self.count += 1
            # print(self.count)
            return
        for i in range(0, self.N):
            if self.isSafe(col, i):
                self.grid[i][col] = 1
                result += self.activityScore[i][col]
                self.nQueens(col+1, result)
                self.grid[i][col] = 0
                result -= self.activityScore[i][col]


    # Calculate Activity score of each cell in grid initially so that we can use it to find out the heuristic value
    def populateActivityScore(self):
        s = self.s
        for time in self.scooterPositions:
            t = 0
            while t < s:
                self.activityScore[int(time[t][0])][int(time[t][1])] += 1
                t = t + 1

    # Recusrive call for placing p police men in n x n grid using A* algorithm, DFS and BackTracking
    def arrangePolice(self, col, p, result):
        # write algorithm for arranging p police in grid and iterate over each such possible grid
        # for each arrangement call countActivityPoints method
        if p == 0:
            # if self.police == self.numberOfOnes():
                # print(self.grid)
                # print(l)
            # self.printBoard(self.grid)
            if(self.score < result):
                self.score = result
            # print(self.score)
            # temp = self.countActivityPoints(self.grid, self.s)
            # if temp > self.score:
            #     self.score = temp
            self.count = self.count + 1
            return
        for j in range(col, self.N):

            for i in range(0, self.N):
                # if p == self.police:
                #     if i > int(self.N/2) + 1:
                #         continue
                # print(j, i)
                # s = calculateMaxScoreSum(col)
                if self.isSafe(j, i):
                    if self.N-j >= p:
                        self.grid[i][j] = 1
                        result += self.activityScore[i][j]
                        p = p - 1
                        h = self.heuristicScore(j, p)
                        # print(result, "  ", h, "   ", result+h, "   ", self.score)
                        if (result + h < self.score):
                            self.grid[i][j] = 0
                            p = p + 1
                            result -= self.activityScore[i][j]
                            continue
                        self.arrangePolice(j + 1, p, result)
                        self.grid[i][j] = 0
                        p = p + 1
                        result -= self.activityScore[i][j]


    # Check if there is a conflict in the grid because of placing a police in position (row, col)
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

    # Calculating heuristic score
    def heuristicScore(self, col, p):
        temp = 0
        list = []
        l = []
        for i in range(col+1, self.N):
            for j in range(0, self.N):
                l.append(self.activityScore[j][i])
            list.append(max(l))
            l=[]
        # print(col, " ", p, " ", self.activityScore.__len__())
        # print(list)
        data = nlargest(p, list)
        temp = sum(data)
        return temp


sol = Solution("input3.txt", "output.txt")
