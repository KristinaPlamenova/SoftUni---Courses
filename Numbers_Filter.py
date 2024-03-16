
def even_odd_filter(**kwargs):
    dictionary = {}
    for key,value in kwargs.items():
        if key == "even":
            dictionary[key] = [n for n in value if n % 2 == 0]
        else:
            dictionary[key] = [n for n in value if n % 2 != 0]
    return dictionary

print(even_odd_filter(
odd=[1, 2, 3, 4, 10, 5],
even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))