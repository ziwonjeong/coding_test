import sys
sys.stdin = open(filname, 'r')

temp = list(map(int, input().split(' ')))
N = temp[0]
M = temp[1]

BLOCK = []
for i in range(0, N):
    BLOCK.append(input().split())