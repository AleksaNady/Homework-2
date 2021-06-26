words = input("введите синонимы для слова Правда через пробел: ").split( )
for ind, el in enumerate(words, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{ind}.{el}")





