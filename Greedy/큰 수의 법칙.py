N, M, K = map(int, input().split())

data = list(map(int, input().split()))
data.sort(reverse=True)

first, second = data[0], data[1]

quot, remainer = divmod(M, K+1)
result = (quot * K + remainer) * first
result += quot * second
print(result)