#(on-going) codeup 4024: 호수의 수 구하기 : https://www.codeup.kr/problem.php?id=4024
from collections import deque


def bfs(rivers, visited, x, y):
    queue = deque([[x, y]])
    while queue:
        pos = queue.popleft()
        row, col = pos
        visited[row][col] = True
        if (0 < row) and (0 < col):
            if (not visited[row-1][col-1]) and (rivers[row-1][col-1] == "L"):
                queue.append([row-1, col-1])
        if (0 < row) and (not visited[row-1][col]) and (rivers[row-1][col] == "L"):
            queue.append([row-1, col])
        if (0 < row) and (col < W-1) and (not visited[row-1][col+1]) and (rivers[row-1][col+1] == "L"):
            queue.append([row-1, col+1])
        if (row < H-1) and (0 < col):
            if (not visited[row+1][col-1]) and (rivers[row+1][col-1] == "L"):
                queue.append([row+1, col-1])
        if (row < H-1) and (not visited[row+1][col]) and rivers[row+1][col] == "L":
            queue.append([row+1, col])
        if (row < H-1) and (col < W-1) and not visited[row+1][col+1] and rivers[row+1][col+1] == "L":
            queue.append([row+1, col+1])
        if  (0 < col) and not visited[row][col-1] and rivers[row][col-1] == "L":
            queue.append([row, col-1])
        if (col < W-1) and (not visited[row][col+1]) and rivers[row][col+1] == "L":
            queue.append([row, col+1])
            
                
                
    

W, H = map(int, input().split())
rivers = []
visited = [[False for _  in range(W)] for _ in range(H)]

for h in range(H):
    rivers.append(input().split())
    
count = 0
for i in range(H):
    for j in range(W):
        if (rivers[i][j] == 'L') and not visited[i][j]:
            bfs(rivers, visited, i, j)
            count += 1

print(count)