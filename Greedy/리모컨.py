# (on going) codeup 3120: 리모컨 https://www.codeup.kr/problem.php?id=3120
temp, new_temp = map(int, input().split())
buttons = [10,5,1]
count = 0

diff_temp = new_temp - temp 
for button in buttons:
    count += (new_temp - temp) // num
    temp %= num
    
print(count)

