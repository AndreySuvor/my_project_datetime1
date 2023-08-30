#Дан режим работы магазина:
#Понедельник	9:00 - 21:00
#Вторник	9:00 - 21:00
#Среда	9:00 - 21:00
#Четверг	9:00 - 21:00
#Пятница	9:00 - 21:00
#Суббота	10:00 - 18:00
#Воскресенье	10:00 - 18:00

#Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут, оставшееся до закрытия магазина.
#На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.
#Программа должна вывести количество минут, которое осталось до закрытия магазина, или текст Магазин не работает, если он закрыт.

from datetime import *
schedule = {
    'Mon': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Tue': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Wed': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Thu': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Fri': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Sat': {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
    'Sun': {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
    }
my_date, my_time = input().split()
my_date = datetime.strptime(my_date, '%d.%m.%Y').strftime('%a')

x = datetime.strptime(my_time, '%H:%M')
x = x.hour * 60 + x.minute

nachalo = str(schedule[my_date]['start']).split(":")
nachalo = (int(nachalo[0]) * 60 + int(nachalo[1]))

zacryt = str(schedule[my_date]['end']).split(":")
zacryt = (int(zacryt[0]) * 60 + int(zacryt[1]))

if x < nachalo or x >= zacryt:
    print('Магазин не работает')
else:
    my_time = my_time.split(":")
    my_time = timedelta(hours=int(my_time[0]), minutes=int(my_time[1]))
    print(int((schedule[my_date]['end'] - my_time).total_seconds() // 60))