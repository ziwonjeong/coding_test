# stack 구조 활용

def dfs(graph, v, visited):
    '''
    graph: 탐색해야할 그래프(자료구조)
    v: 탐색할 node
    visited: 탐색했던 node
    '''
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
            
        
# graph examples
graph = [   [],
            [2,3,8],
            [1,7],
            [1,4,5],
            [3,5],
            [3,4],
            [7],
            [2,6,8],
            [1,7]
]

visited = [False] * 9
dfs(graph, 1, visited)