# (Done) codeup 3301: https://www.codeup.kr/problem.php?id=3301

money_box = [50000,10000,5000,1000,500,100,50,10]

payment = int(input())

result = 0
for money in money_box:
    count, remainder = divmod(payment, money)
    if not count:
        continue
    else:
        result += count
        payment = remainder
        if not remainder:
            break 
        
print(result)