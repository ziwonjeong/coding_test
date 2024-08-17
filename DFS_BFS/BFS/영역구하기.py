# (on-going) codeup 4572: 영역 구하기 https://www.codeup.kr/problem.php?id=4572
from collections import deque
def bfs(x, y, arr):
    queue = deque([[x, y]])
    count = 0
    while queue:
        row, col = queue.popleft()
        arr[row][col] = 1
        print(f'{row=}, {col=}')
        count += 1
        if (0 < row) and (arr[row-1][col] == 0):
            queue.append([row-1, col])
        if (0 < col) and (arr[row][col-1] == 0):
            queue.append([row, col-1])
        if (row < len(arr)-1) and (arr[row+1][col] == 0):
            queue.append([row+1, col])
        if (col < len(arr[0])-1) and (arr[row][col+1] == 0):
            queue.append([row, col+1])
    return count

N, M, K = map(int, input().split())

arr = [[0 for _ in range(M)] for _ in range(N)]

 
for k in range(K):
    x, y, x_, y_ = map(int, input().split())
    for i in range(x, x_):
        for j in range(y, y_):
            print(i,j)
            if arr[i][j] == 0:
                arr[i][j] = 1
                
from pprint import pprint
pprint(arr)
 
count = 0
for i in range(N):
    for j in range(M):
        print(i, j)
        if arr[i][j] == 0:
            count += bfs(i, j ,arr)


print(count)