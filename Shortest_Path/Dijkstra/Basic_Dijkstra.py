import heapq
import sys
# input = sys.stdin.readline.rstrip()

INF = int(1e9) 
breakpoint()
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)] # 그래프 초기화 (2차원 리스트)
distance = [INF] * (n + 1) # 최단 거리 테이블 초기화

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # 방향 그래프
    # graph[v].append((u, w)) # 무방향 그래프

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로는 0
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) 
        if distance[now] < dist: 
            continue

        for i in graph[now]: 
            cost = dist + i[1] 
            if cost < distance[i[0]]: 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) 


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

