import sys
from copy import deepcopy

if sys.platform == 'win32':                 # window 환경에서만 동작
    sys.stdin = open('input.txt')           # input date를 text 파일에서만 읽어오기

input = sys.stdin.readline                  # 데이터 입력 속도 향상

MAXN = 1005
W, H = map(int, input().split())            # 도형의 너비와 높이
arr = [[''] * MAXN for _ in range(MAXN)]     # 도형 2차원 배열
tmp = [[''] * MAXN for _ in range(MAXN)]     # 임시 도형 2차원 배열

def rotate90():
    global W, H
    # tmp = deepcopy(arr)                     # 임시로 배열 저장
    for r in range(H): tmp[r] = arr[r][:W]

    # W, H가 바뀌어서 수행
    W, H = H, W
    for r in range(H):
        for c in range(W):
            arr[r][c] = tmp[W - 1 - c][r]

def rotate180():
    tmp = deepcopy(arr)                     # 임시로 배열 저장

    for r in range(H):
        for c in range(W):
            arr[r][c] = tmp[H - 1 - r][W - 1 - c]

def rotate270():
    global W, H
    # tmp = deepcopy(arr)                     # 임시로 배열 저장
    for r in range(H): tmp[r] = arr[r][:W]

    # W, H가 바뀌어서 수행
    W, H = H, W
    for r in range(H):
        for c in range(W):
            arr[r][c] = tmp[c][H - 1 - r]

def flipUD():
    for r in range(H // 2):
        for c in range(W):
            arr[r][c], arr[H - 1 - r][c] = arr[H - 1 - r][c], arr[r][c]

def flipLR(): 
    for r in range(H):
        for c in range(W // 2):
            arr[r][c], arr[r][W - 1 - c] = arr[r][W - 1 - c], arr[r][c]

# 도형 입력 받기
for r in range(H):
    data = input().strip()
    for c in range(W):
        arr[r][c] = data[c]

cmd = int(input())

if cmd == 0: rotate90()
if cmd == 1: rotate180()
if cmd == 2: rotate270()
if cmd == 3: flipUD()
if cmd == 4: flipLR()

# 결과 출력
print(W, H)
for r in range(H): print(*arr[r][:W], sep="")
