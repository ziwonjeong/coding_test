# (on going) codeup 3321: https://www.codeup.kr/problem.php?id=3321

num_of_toppings = int(input())
dough_price, topping_price = map(int, (input().split()))
dough_calories = int(input())

topping_calories = []
for topping in range(num_of_toppings):
    topping_calories.append(int(input()))

result = dough_calories / dough_price
for i in range(1 << num_of_toppings):
    topping_subset = []
    for j in range(num_of_toppings):
        if i & (1<<j):
            topping_subset.append(topping_calories[j])
            pizza_cal = sum(topping_subset) + dough_calories
            pizza_pri = dough_price + topping_price * len(topping_subset)
            if result < pizza_cal / pizza_pri:
                result = pizza_cal / pizza_pri
            

print(int(result))

        

# reference about sub set: https://velog.io/@94applekoo/%EB%B9%84%ED%8A%B8%EC%97%B0%EC%82%B0%EC%9E%90%EB%A1%9C-%EB%B6%80%EB%B6%84-%EC%A7%91%ED%95%A9%EC%9D%84-%EC%83%9D%EC%84%B1%ED%95%98%EB%8A%94-%EB%B2%95-python
