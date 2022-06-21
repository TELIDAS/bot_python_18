"""
Есть у нас список учеников которые сдавали тест
Нужно вывести средний балл всех учеников ,
этот результат надо сравнить со своим баллом
Если ваш балл ниже среднего значит надо вернуть False
Если ваш балл выше надо вернуть True
"""


def better_than_average(class_points, your_points):
    return "You r smarter than average of your class" if (sum(class_points) / len(
        class_points)) < your_points else "You r not smarter than average of your class"

    # if (sum(class_points) / len(class_points)) < your_points:
    #     return True
    # else:
    #     return False


class_points = [2, 4, 100, 70, 40, 66]
your_points = 46
# print(better_than_average(class_points, your_points))


"""
Вы решили отправиться на отдых в Сейшельские острова
Там вам понадобилось арендовать машину
Арендатель говорит , аренда авто в день стоит 40$
Если вы будете арендовать больше или равно 7 дней , дает скидку 50$
Если вы арендуете меньше 7 дней но больше 3 дней, он все равно дает 20$
"""


def seyshely_vacation(d):
    pass


days_1 = 2
days_2 = 4
days_3 = 8
print(seyshely_vacation(days_3))

"""
Нужно создать  функцию конвертер валют с доллара на юань
Конвертирует по курсу 6.75

Вывод :
15 долларов то он должен вернуть 101.25
465 долларов 

Неправильный вывод:
101.256

Условие задачи в том чтобы возвращал только две цифры после запятой
Это нужно сделать в одну строку
"""


def converter(usd):
    pass


usd = 15
print(converter(usd))
