import sys
if sys.platform == 'darwin':
    sys.stdin = open('/Users/ziwon/Desktop/git/coding_test/sample_input.txt')

input = sys.stdin.readline

T = int(input())
grid = [[False] * 100 for _ in range(100)]
for _ in range(T):
    W, H = map(int, input().split())
    for h in range(H, H+11):
        for w in range(W, W+11):

            grid[h][w] = True

ans = 0 
for h in range(99):
    for w in range(99):
        if (grid[h][w] != grid[h][w+1]):
            ans += 1
        if (grid[h][w] != grid[h+1][w]):
            ans += 1

print(ans)