
def even_odd(*args):
    command = args[-1]

    nums = []
    if command == "even":
        nums = [n for n in args[:-1] if n % 2 == 0]
    elif command == "odd":
        nums = [n for n in args[:-1] if n % 2 != 0]
    return nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
