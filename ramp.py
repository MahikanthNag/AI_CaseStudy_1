import time
import numpy
from numpy import array
# import scipy as sp
# from scipy import sparse

max_score = 0
scoring = 0
scoringt = 0
data = []
activity_score = []
counting = 0
p_main = 0
# input
t0 = time.clock()
with open('input1.txt', 'r') as fp:
    count = 1
    for line in fp:
        line = line.rstrip('\n')
        if count == 1:
            n = int(line)
        if count == 2:
            p = int(line)
            p_main = p
        if count == 3:
            s = int(line)
        if count > 3:
            line = line.strip()
            data.append(line)
        count += 1


def calculate_activity(data):
    global n
    for i in range(len(data)):
        x = int(data[i][0])
        y = int(data[i][2])
        activity_score[x][y] += 1
    # sparse_m=sp.sparse.lil_matrix((n,n))
    # sparse_m=sp.sparse.lil_matrix(activity_score)
    # print sparse_m
    print
    activity_score


# instialising the b
def instialising(n):
    b = [0] * n
    for x in range(n):
        b[x] = [0] * n
    return b


# storing policemen postions
def all_positions(b):
    global max_score, n
    # print b
    x = check_score(b, n, data)
    # print x
    if max_score < x:
        max_score = x


# global ans
# test=copy.deepcopy(b)
# ans.append(test)


# printing all solutions
# def all_solutions(ans,n):
# 	for s in ans:
# 		for row in s:
# 			print row
# 		print "\n"
# checking if valid or not
def check(b, r, c, n):
    # checking columns for match
    for i in range(c):
        if b[r][i] == 1:
            return False
    # checking left diagonals
    tr = r
    tc = c
    while tc >= 0 and tr >= 0:
        if b[tr][tc] == 1:
            return False
        tc -= 1
        tr -= 1
    t1 = r
    t2 = c
    while t2 >= 0 and t1 < n:
        if b[t1][t2] == 1:
            return False
        t2 -= 1
        t1 += 1
    return True


# placing of policemen
def placement(b, n, y, p, scoring, scoringt):
    global counting, max_score
    global p_main
    if p == 0:
        counting = counting + 1
        # all_positions(b)
        # print max(scoring,scoringt)
        if max_score < max(scoring, scoringt):
            max_score = max(scoring, scoringt)
            scoring = 0
            scoringt = 0
        return
    for j in range(y, n):
        for i in range(n):
            if p == p_main:
                if i > int(n / 2) + 1:
                    continue
            if check(b, i, j, n) and n - y >= p:
                b[i][j] = 1
                scoring = scoring + activity_score[i][j]
                scoringt = scoringt + activity_score[j][i]
                p -= 1
                # if y==n-1 or p==0:
                # 	all_positions(b)
                # 	b[i][y] = 0
                # 	return
                placement(b, n, j + 1, p, scoring, scoringt)
                b[i][j] = 0
                p += 1
                scoring = scoring - activity_score[i][j]
                scoringt = scoringt - activity_score[j][i]


# checking score
# def check_score(b,n,data):
# 	global activity_score
# 	score=0
# 	score_trans=0
# 	trans= numpy.transpose(b)
# 	global max_score
# 	for i in range(0,n):
# 		for j in range(0,n):
# 			if b[i][j]==1:
# 				score+=activity_score[i][j]
# 			if trans[i][j]==1:
# 				score_trans+=activity_score[i][j]
# 		#print i
# 		# print str(data[i][2])+"check these"
# 		# print ""+str(b[int(data[i][0])][int(data[i][2])])
# 		# if b[int(data[i][0])][int(data[i][2])]==1:
# 		# 	score+=1
# 		# i+=1
# 	if score_trans<score:
# 		return score
# 	else:
# 		return score_trans


b = instialising(n)
activity_score = instialising(n)
# calculate_activity(data)
activity_score = [[38, 2, 42, 12, 16, 24, 42, 15, 15, 31, 39], [31, 31, 17, 16, 15, 30, 36, 39, 43, 20, 19],
                  [9, 8, 20, 16, 48, 39, 39, 25, 5, 45, 22], [19, 23, 39, 17, 25, 24, 38, 27, 48, 17, 24],
                  [25, 45, 12, 38, 17, 7, 4, 15, 50, 42, 39], [37, 30, 7, 50, 7, 43, 37, 41, 18, 38, 6],
                  [41, 45, 0, 39, 15, 11, 2, 20, 1, 33, 11], [48, 9, 48, 34, 47, 8, 27, 29, 41, 46, 41],
                  [2, 26, 9, 34, 2, 7, 49, 50, 24, 19, 40], [46, 50, 3, 40, 30, 22, 15, 22, 44, 34, 45],
                  [26, 37, 48, 32, 0, 43, 48, 11, 47, 16, 32]]

placement(b, n, 0, p, scoring, scoringt)
# print counting
# all_solutions(ans,n)
# print str(counting)+"is the total solution"
print
max_score
print
time.clock() - t0, "seconds process time"

# print data
# output
with open("output.txt", 'w') as text:
    text.write(str(max_score))




