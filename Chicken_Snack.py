from collections import deque
eaten_food = 0
money = [int(el) for el in input().split()]
price_of_food = deque(int(el) for el in input().split())
change = 0

while money and price_of_food:
    current_money = money[-1]
    current_price = price_of_food[0]
    if current_money == current_price:
        money.pop()
        price_of_food.popleft()
        eaten_food += 1

    elif current_money > current_price:
        change = current_money - current_price
        money.pop()
        if money:
            money[-1] += change
        price_of_food.popleft()
        eaten_food += 1


    else:
        money.pop()
        price_of_food.popleft()


if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
elif eaten_food == 1:
    print(f"Henry ate: {eaten_food} food.")
elif eaten_food == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif eaten_food < 4:
    print(f"Henry ate: {eaten_food} foods.")
















