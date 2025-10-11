import sys

if sys.platform == 'win32': # window 환경에서만 동작
    sys.stdin = open('answer.txt')

programs = [0] * 1000000

Q = int(input())
for q in range(Q):
    order, *value = list(input().split())
    if order == 'add':
        _id, s, e = map(int, value)
        if _id not in set(programs) and any(programs[s:e+1]) == False:
            for i in range(s, e+1):
                programs[i] = _id

    elif order == 'getCnt':
        date = int(value[0])
        cnt = set(programs[:date])
        cnt.discard(0)
        print(len(cnt))

    else:
        date = int(value[0])
        if programs[date] != 0:
            print(programs[date])
        else:
            print(-1)
            
