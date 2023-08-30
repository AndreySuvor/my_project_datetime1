#Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00.
#Напишите программу, которая принимает на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.

#Формат входных данных:
#На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.
#Формат выходных данных:
#Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в следующем формате:
#До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов
#Если в данном случае количество часов равно нулю, то вывести нужно только дни.
#Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:
#До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут
#Если в данном случае количество минут равно нулю, то вывести нужно только часы. Аналогично, если количество часов равно нулю, то вывести нужно только минуты.
#Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна вывести текст: Курс уже вышел!


from datetime import *

my_date = input().replace(":", '.').replace('.', ' ').split()
current = datetime(int(my_date[2]), int(my_date[1]), int(my_date[0]), int(my_date[3]), int(my_date[4]))
x = datetime(2022, 11, 8, 12, 0)
delta = x - current

def choose_plural(amount, declensions):
    a = [2, 3, 4]
    if amount % 10 == 1 and (amount % 100) // 10 != 1:
        return f'{amount} {declensions[0]}'
    elif amount % 10 in a and (amount % 100) // 10 != 1:
        return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[2]}'

day = delta.days
hour = delta.seconds // 3600
minit = delta.seconds // 60 % 60

my_dict = {0: ("день", "дня", "дней"), 1: ("час", "часа", "часов"), 2: ("минута", "минуты", "минут")}

if day < 0:
    print("Курс уже вышел!")
else:
    if day == 0:
        if hour == 0:
            if minit == 0:
                print("Курс уже вышел!")
            else:
                print(f"До выхода курса осталось: {choose_plural(minit, my_dict[2])}")
        else:
            if minit == 0:
                print(f"До выхода курса осталось: {choose_plural(hour, my_dict[1])}")
            else:
                print(f"До выхода курса осталось: {choose_plural(hour, my_dict[1])} и {choose_plural(minit, my_dict[2])}")
    else:
        if hour == 0:
            if minit == 0:
                print(f"До выхода курса осталось: {choose_plural(day, my_dict[0])}")
            else:
                print(f"До выхода курса осталось: {choose_plural(day, my_dict[0])}")
        else:
            if minit == 0:
                print(f"До выхода курса осталось: {choose_plural(day, my_dict[0])} и {choose_plural(hour, my_dict[1])}")
            else:
                print(f"До выхода курса осталось: {choose_plural(day, my_dict[0])} и {choose_plural(hour, my_dict[1])}")