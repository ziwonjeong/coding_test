T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    
    containers.sort()
    trucks.sort()
    
    result = 0
    while (containers and trucks):
        container = containers.pop()
        truck = trucks.pop()
        if container > truck:
            trucks.append(truck)
            continue
        else:
            result += container
    
    print(f'#{t} {result}')
        