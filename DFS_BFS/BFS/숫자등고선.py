# (Done) codeup 1512: 숫자 등고선 https://www.codeup.kr/problem.php?id=1512

# N: 배열의 크기 / X,Y: 시작위치
# next_visted : 갈 수 있는 case
## 0이 아니고, 갈 수 있는 곳이면 이동

from collections import deque

def bfs(x, y, arr):
    queue = deque([[x, y]])
    arr[x][y] = 1

    while queue:
        pos = queue.popleft()
        row, col = pos
        if 0 < row:
            if arr[row-1][col] == 0:
                arr[row-1][col] = arr[row][col] + 1
                queue.append([row-1, col])
                
        if 0 < col:
            if arr[row][col-1] == 0:
                arr[row][col-1] = arr[row][col] + 1
                queue.append([row, col-1] ) 
                
        if row < len(arr)-1:
            if arr[row+1][col] == 0:
                arr[row+1][col] = arr[row][col] + 1
                queue.append([row+1, col])
                
        if col < len(arr)-1:
            if arr[row][col+1] == 0:
                arr[row][col+1] = arr[row][col] + 1
                queue.append([row, col+1])
                
                       
                      
            
arr_n = int(input())
arr = [[0 for _ in range(arr_n)] for _ in range(arr_n)]

x, y = map(int, input().split())

bfs(x-1 ,y-1, arr)


for i in arr:
    i = [str(c) for c in i]
    print(' '.join(i))

