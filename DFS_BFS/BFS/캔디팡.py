# (Done) codeup 2605: 캔디팡 https://www.codeup.kr/problem.php?id=2605

from collections import deque

def bfs(x, y, arr, visited):
    queue = deque([[x, y]])
    visited[x][y] = 1
    count = 1
    while queue:
        pos = queue.popleft()
        row, col = pos
        if 0 < row:
            if (arr[row-1][col] == arr[row][col]) and (visited[row-1][col] == 0):
                count += 1
                visited[row][col+1] = 1
                queue.append([row-1, col])
                
        if 0 < col:
            if (arr[row][col-1] == arr[row][col]) and (visited[row][col-1] == 0):
                count += 1
                visited[row][col-1] = 1
                queue.append([row, col-1] ) 
                
        if row < len(arr)-1:
            if (arr[row+1][col]  == arr[row][col]) and (visited[row+1][col] == 0):
                count += 1
                visited[row+1][col] = 1
                queue.append([row+1, col])
                
        if col < len(arr)-1:
            if (arr[row][col+1]  == arr[row][col]) and (visited[row][col+1] == 0):
                count += 1
                visited[row][col+1] = 1
                queue.append([row, col+1])               
    return count, visited
    
arr = []
for i in range(7):                     
    row = input().split()
    row = [int(i) for i in row]
    arr.append(row)

visited = [[0 for _ in range(7)] for _ in range(7)]

clear = 0
for i in range(7):
    for j in range(7):
        if visited[i][j] == 0:
            count, visited = bfs(i, j, arr, visited)
            if count >= 3:
                clear += 1
        else:
            continue
                
print(clear)