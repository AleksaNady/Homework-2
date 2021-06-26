my_list = [7, 5, 3, 3, 2]
number = int(input('введите следующее число рейтинга:  '))
i = 0
for element in my_list:
    if number <= element:
        i += 1
    else:
        break
my_list.insert(i, number)
print(my_list)


