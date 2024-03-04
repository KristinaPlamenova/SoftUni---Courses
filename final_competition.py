count_dancers = int(input())
count_points = float(input())
season = input()
place = input()
win_money = 0
money_for_dancer = count_dancers * count_points


if place == "Bulgaria":
    if season == "summer":
        win_money = money_for_dancer * 0.95
    elif season == "winter":
        win_money = money_for_dancer * 0.92
elif place == "Abroad":
    if season == "summer":
        win_money = (money_for_dancer * 1.5) * 0.90
    elif season == "winter":
        win_money = (money_for_dancer * 1.5) * 0.85


charity = win_money * 0.75
left_money = win_money - charity
money_for_one_dancer = left_money / count_dancers

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_for_one_dancer:.2f}")

