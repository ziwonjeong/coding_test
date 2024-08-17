# (Done) codeup 4503: 바이러스 https://www.codeup.kr/problem.php?id=4503

def dfs(v, count):
    '''
    graph: 탐색해야할 그래프(자료구조)
    v: 탐색할 node
    visited: 탐색했던 node
    '''

    visited[v] = True
    for i in computers[v]:
        if not visited[i]:
            count += 1
            count = dfs(i, count)
    return count

num_computers = int(input())
N = int(input())
computers = [[] for _ in range(num_computers+1)]
visited = [False] * (num_computers + 1)


for i in range(N):
    x, y = map(int, input().split())
    computers[x].append(y)
    computers[y].append(x)

count = 0 
count = dfs(1, count)
print(count)