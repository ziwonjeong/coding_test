# (on going) codepass 3431: 개구리점프 https://www.codepass.co.kr/bbs/bbs_view_quest.php?prod_idx=2753
def check_next_point(logs, visited, start, end):
    x, xp, y = logs[start]
    visited[start] = True
    if start == end:
        return 1
    for i, (nx, nxp, ny) in enumerate(logs):
        if not visited[i]:
            if nx in range(x, xp+1):
                return check_next_point(logs, visited, i, end)
            elif nxp in range(x, xp+1):
                return check_next_point(logs, visited, i, end)
        else: # 방문한 적 있음
            continue
    return 0 
    

N, Q = map(int, input().split())
logs = [[0,0,0]]
for n in range(N):
    logs.append(list(map(int, input().split())))
      
result = []
for ques in range(Q):

    visited = [False] * len(logs)
    visited[0] = True
    flag = True

    start, end = map(int, input().split())
    while flag:
        res = check_next_point(logs, visited, start, end)
        result.append(res)
        flag = False
        
for res in result:
    print(res)
        
        
# reference: https://velog.io/@young_gyu/Python-%EB%B0%B1%EC%A4%80-17619-%EA%B0%9C%EA%B5%AC%EB%A6%AC-%EC%A0%90%ED%94%84