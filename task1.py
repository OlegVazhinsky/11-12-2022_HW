"""

Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:
- 6 -> да
- 7 -> да
- 1 -> нет

"""

def is_number_of_week(week_day):
    if 0 < week_day < 8:
        return week_day
    else:
        return 0

def is_number_of_weekend(week_day):
    if week_day == 6:
        return 'суббота'
    elif week_day == 7:
        return 'воскресенье'
    else:
        return 0


user_week_day = int(input('Введите число, соответствующее дню недели -> '))
if is_number_of_week(user_week_day) != 0:
    if is_number_of_weekend(user_week_day) !=0:
        print(f'Введенное число соответствует дню недели - {is_number_of_weekend(user_week_day)}.')
    else:
        print('Введенное число соответствует буднему дню недели.')   
else:
    print('Введенное число не соответствует ни одному дню недели.')