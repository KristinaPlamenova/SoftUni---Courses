count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarian = int(input())
price_for_chicken_menu = count_chicken_menu * 10.35
price_for_fish_menu = count_fish_menu * 12.40
price_for_vegetarian_menu = count_vegetarian * 8.15
all_price_menu = price_for_chicken_menu + price_for_fish_menu + price_for_vegetarian_menu
price_desert = 0.2 * all_price_menu
total_price = all_price_menu + price_desert + 2.50
print(total_price)