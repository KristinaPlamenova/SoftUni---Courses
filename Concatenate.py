
def concatenate(*args, **kwargs):
    words = ''.join(args)

    for key, value in kwargs.items():
       words = words.replace(key, value)

    return words

