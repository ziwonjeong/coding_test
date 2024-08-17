# (on-going) codeup 2062: Up 2 https://www.codeup.kr/problem.php?id=2062
def dfs(house, visited, x, y, val):           
    stack = [[x,y]]
    while stack:
        x_, y_ = stack.pop()
        visited[x_][y_] = True 

        
        

m, n = map(int, input().split())
balloon = {}
house = []
visied = [[False for _ in range(n)] for _ in range(m)]

for i in range(n):
    for j in input().split():
