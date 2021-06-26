

while True:
    month = input("Введите месяц: ")
    if month.isdigit () and 0 < int(month) <=12:
        seasons_list = ['зима', 'весна', 'лето', 'осень']
        seasons_dic  = {0:'зима' , 1:'весна' , 2:'лето' , 3:'осень', 4:'зима'}
        print(f'список сезонов - {seasons_list[int(month) // 3]}\ncловарь сезонов - {seasons_dic[int(month) // 3]}')
        break
    else:
        print("ошибка")


