# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('hi world')
print("Привет, я Анфиса!")
friends = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']
friends_string = ', '.join(friends)
print('Твои друзья:', friends_string)
stations = ['Москва', 'Серп и Молот', 'Карачарово', 'Чухлинка', 'Кусково', 'Новогиреево', 'Реутово', 'Никольское', 'Салтыковская', 'Кучино', 'Железнодорожная', 'Чёрное', 'Купавна', '33-й километр', 'Электроугли', '43-й километр', 'Храпуново', 'Есино', 'Фрязево', '61-й километр', '65-й километр', 'Павлово-Посад', 'Назарьево', 'Дрезна', '85-й километр', 'Орехово-Зуево', 'Крутое', 'Воиново', 'Усад', '105-й километр', 'Покров', '113-й километр', 'Омутище', 'Леоново', 'Петушки']

# напишите свой код здесь
print(' - '.join(stations))
around_zero = range(-3, 3)

# Вместо списка в цикл передаётся переменная around_zero,
# в ней хранится range() от -3 до 3
for i in around_zero:
    # Перебрать все числа в диапазоне от -3 до 3 и напечатать их:
    print(i)
# Будет напечатано
# -3
# -2
# -1
# 0
# 1
# 2
for i in range(1,5):
	print('Я расправлюсь с задачей', str(i))

print('Я всех победю!')
print('Это первый этаж.')
# Первый этаж построен, начинайте строить со второго
for i in range(2,11):
    # Здесь вместо многоточий
    # вставьте номер текущего этажа,
    # вычислите и вставьте номер предыдущего этажа.
    print('А это', str(i), 'этаж, он на один выше, чем этаж', str((i-1)))
    bunny_counter = ''  # Создали переменную bunny_counter, её значение - пустая строка.

    for i in range(1, 6):
        # На каждой итерации цикла
        # к переменной bunny_counter будет дописываться
        # очередная цифра, запятая и пробел (чтобы числа в строке не слиплись).
        # Получившееся значение будет присвоено той же переменной bunny_counter
        bunny_counter = bunny_counter + str(i) + ', '

    print(bunny_counter + 'вышел зайчик погулять!')
    countdown_str = ''

    for i in reversed(range(0, 11)):
        countdown_str = countdown_str + str(i) + ', '

    countdown_str = countdown_str + 'поехали!'

    print(countdown_str)
    
    
z=1+1j
w=2-3j
print(z*w)
#elif — это вложенная конструкция для if: «если условие для if не выполнено, но выполняется условие для elif — выполнить код в блоке elif»

for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count <= 4:
        print('У вас', messages_count, 'новых сообщения')
    else:
        print('У вас', messages_count, 'новых сообщений')
for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    if current_hour < 6:
        print('Доброй ночи!')
    elif  current_hour < 12:
        print ('Доброе утро!')
    elif current_hour < 18:
        print ('Добрый день!')
    elif current_hour < 23:
        print ('Добрый вечер!')
    else:
        print('Доброй ночи!')
     # Кроме простых операторов сравнения  «равно» ==,«меньше» <, «больше» >,  и более сложные операторы, учитывающие сразу два условия: больше или равно >=, меньше или равно <=, не равно !=.##
for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif  messages_count == 1:
        # напишите ваш код здесь
        print ('У вас', messages_count, 'новое сообщение')
    elif messages_count == 4 or messages_count <= 3:
        # напишите ваш код здесь
         print ('У вас', messages_count, 'новых сообщения')
    else:
        # напишите ваш код здесь
         print ('У вас', messages_count, 'новых сообщений')
         wind = True

# Есть ли ветер?
if not wind: # Если wind НЕ равен True
    print('Ночь тиха')
else:
    print('Поднялся ветер')
    print('Серые тучи развеял')
    print('Новые тянутся с юга')
# передадим в программу данные
beaufort = 6  # сильный ветер
is_raining = False  # дождя нет
temperature = 16

if (not is_raining or beaufort <= 4) and temperature > 22:
    print('Идём гулять, на улице хорошо')
else:
    print('Сидим дома, читаем Практикум')
    good_boy = True  # Мальчик-то неплохой

if not good_boy:
    print('Этот в грязь полез')
    print('и рад,')
    print('что грязна рубаха.')
    print('Про такого говорят:')
    print('он плохой, неряха.')
else:
    print('Этот чистит валенки,')
    print('моет сам галоши.')
    print('Он хотя и маленький,')
    print('но вполне хороший.')
# Продуктов маловато:
milk = not True       # Молоко "НЕ есть".
cereals = True        # Хлопья есть.
eggs = False          # Яиц нет.

# Вставьте логический оператор вместо многоточия.
# Решите, нужно ли расставить скобки.

if milk and cereals or eggs:
    if eggs:
        if milk:
            breakfast = "- омлет"
        else:
            breakfast = "- яичница"
    else:
        breakfast = "- хлопья с молоком"
else:
    if milk:
        breakfast = "- стакан молока"
    elif cereals:
        breakfast = "можно погрызть сухих хлопьев"
    else:
        breakfast = "ничего не будет: разгрузочный день"
# Объявление функции hello()
def hello(name, bonus):
    # А здесь началось тело функции
    print(name + ', Приветствую тебя! Бери', bonus) 
hello('Рома', 'Член в рот')
hello('Nika', 'Член в рот')
# Код функции say_hello()
def say_hello(current_hour):
    if current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')
    elif current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')

# Дальше код написан без отступов: этот код уже вне функции.

# Несколько раз вызовем функцию say_hello() с разными аргументами:
say_hello(4)  # Вызов функции say_hello() с аргументом 4
say_hello(10)  # Вызов функции с аргументом 10
say_hello(15)  # Ещё один вызов функции
say_hello(20)  # И ещё один вызовx
# Объявите функцию здесь
def print_friends_count(friends_count):
	if friends_count == 0:
            print('У тебя нет друзей')
	elif friends_count == 1:
        	print('У тебя', friends_count, 'друг')
	elif friends_count >= 2 and friends_count <= 4:
        	print('У тебя', friends_count, 'друга')
	elif friends_count >= 5 and friends_count < 20:
        	print('У тебя', friends_count, 'друзей')
	else:
        	print('Ого, сколько у тебя друзей! Целых', friends_count)
for friends_count in range(0,21):
	(print_friends_count(friends_count))   
        


def print_home(name, planet):
    print(name + ' живет на планете ' + planet)

tatooin = 'Татуин'
greeting = 'Да пребудет с тобой Сила!'
my_son = 'Люк, я твой отец!'
luke = 'Люк Скайуокер'
# Вызов функции
print_home(luke, tatooin) 

# Если при вызове забудут передать имя - значением name будет слово 'Инкогнито';
# а если вызвать функцию, не передав название планеты -
# функция присвоит переменной planet значение "Икс"
def print_house(name='Инкогнито', planet='Икс'):
    print(name + ' живёт на планете ' + planet)

# Передаём только один аргумент вместо двух
print_house('Дроид-убийца')

# Добавим значение по умолчанию для аргумента name
def print_home(name='Инкогнито', planet='Икс'):
    print(name + ' живёт на планете ' + planet)

# Передаём именованный параметр: 
# явно указываем, что значение 'Земля' предназначено для параметра planet
print_home(planet='Земля')  

# Ещё раз вызовем функцию: передадим два именованных параметра,
# но не в том порядке, как они указаны в объявлении функции:
print_home(planet='Земля', name='Винни Пух')  


# Настройте функцию так, чтобы она не сломалась при вызове без аргументов
def lets_go(name = 'Друг', target = 'учить Python'):
    print(name + ', пойдём ' + target)


# Этот вызов сработает без ошибок в любом случае
lets_go('Гарри', 'ловить Волан-де-Морта')

# Вызовите функцию lets_go без аргументов
lets_go()


def lets_go(name='Друг', target='учить Python'):
    print(name + ', пойдём ' + target)


# Исправьте вызов так, чтобы аргумент был передан
# в параметр с именем target
lets_go(target='читать следующий урок!')





flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

# Сохраним искомое значение в переменной, так будет проще работать.
room_size = 22.19

# В переменной count будем подсчитывать 
# количество обнаруженных помещений нужной площади.
# Пока что она равна нулю.
count = 0

# Объявляем цикл: из списка flat все значения по очереди будут передаваться
# в переменную room
for room in flat:
    # Проверяем, равно ли значение переменной room искомому значению 
    if room == room_size:
        # Если значения room и room_size равны -
        # переменной count присваиваем её предыдущее значение,
        # увеличенное на единицу
        count = count + 1

# Этот код выполнится только после того, 
# как цикл переберёт все элементы списка flat.
# В переменной count будет сохранено количество помещений с площадью 22.19
print('Комнат площадью', room_size, 'кв.м:', count)



flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

# В переменной sum_area будем суммировать площади комнат.
# Пока что она равна нулю.
sum_area = 0

for room in flat:
    # На каждой итерации цикла прибавляем к sum_area площадь ещё одной комнаты
    # Запишем эту операцию через сокращённый синтаксис +=
    sum_area += room

print('Общая площадь =', sum_area)



# Список годов, в которые Depeche Mode выпускала альбомы
years = [
    1981, 1982, 1983, 1984, 1986, 1987, 1990,
    1993, 1997, 2001, 2005, 2009, 2013, 2017
]

# В этой переменной будем подсчитывать количество альбомов.
# Пока что в ней ничего нет, она равна нулю.
count = 0

for year in years:
    if year > 2000:
        # Каждый раз загибаем по одному пальцу,
        # обнаружив альбом, выпущенный в 21 веке.
        count += 1   # это то же самое, что 'count = count + 1'

print('Выпущено альбомов в XXI веке:', count)



# Список годов, в которые Depeche Mode выпускала альбомы
years = [
    1981, 1982, 1983, 1984, 1986, 1987, 1990,
    1993, 1997, 2001, 2005, 2009, 2013, 2017
]

# В этой переменной будем подсчитывать количество альбомов.
# Пока что в ней ничего нет, она равна нулю.
count = 0

for year in years:
    if year > 2000:
        # Каждый раз загибаем по одному пальцу,
        # обнаружив альбом, выпущенный в 21 веке.
        count += 1   # это то же самое, что 'count = count + 1'

print('Выпущено альбомов в XXI веке:', count)

def number_of_occurrences(char, string):
    # Здесь объявите переменную count, равную нулю.
    # Она будет хранить количество вхождений
    count = 0
    for letter in string:
        # Напишите условие: сравните переменные letter и char
        # И если letter равна char - увеличивайте счётчик count на 1
        	if letter == char:
                	count += 1

    # Печатаем исходную строку:
    print('Исходная строка:', string)
    # Печатаем результат подсчётов:
    print('Количество вхождений символа', char, 'составляет:', count)
    

# Код ниже не изменяйте
phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'

# Вызываем функцию number_of_occurrences(), чтобы она посчитала, 
# сколько раз во фразе phrase встречается буква 'е'
number_of_occurrences('е', phrase)










# Функция для вычисления площади прямоугольника;
# от англ. calculate, «вычислять»
def calc_square(side_a, side_b):
    # Вычисляем площадь и присваиваем результат переменной result
    result = side_a * side_b
    # Функция возвращает значение переменной result:
    return result

# Вызываем функцию calc_square() с аргументами 16 и 9. 
# Значение, которое вернёт функция, будет присвоено переменной rectangle_area
rectangle_area = calc_square(16, 9)

print(rectangle_area)



# Функция для вычисления периметра кубов.
def calc_cube_perimeter(side):
    return side * 12


# Функция для вычисления площади кубов.
def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area


# Дополните объявление функции: 
# теперь должна принимать два параметра -
# длину ребра куба и количество кубов.
def calc_cube(side, amount):
    # Вызываем функцию, рассчитывающую периметр
    # и передаём в неё размер куба
    one_cube_perimeter = calc_cube_perimeter(side)

    # Здесь вместо многоточия должна стоять переменная, 
    # хранящая количество кубов, переданное во втором аргументе.
    full_length = one_cube_perimeter * amount

    # Вызываем функцию, рассчитывающую площадь стекла
    # и передаём в неё размер куба
    one_cube_area = calc_cube_area(side)

    # Здесь вместо многоточия должна стоять переменная, 
    # хранящая количество кубов, переданное во втором аргументе.
    full_area = one_cube_area * amount

    # В этой строке замените многоточие на переменную, хранящую количество кубов
    print('Для', amount, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)


# Для проверки работы кода вызываем функцию с двумя аргументами: 
# 3 - это размер ребра куба,
# 2 - это необходимое количество кубов
calc_cube(3, 2)


import numpy as np
import matplotlib.pyplot as plt
 
x = np.random.randint(low=1, high=11, size=50)
y = x + np.random.randint(1, 5, size=x.size)
data = np.column_stack((x, y))
 
fig, (ax1, ax2) = plt.subplots(
    nrows=1, ncols=2,
    figsize=(8, 4)
)
 
ax1.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
ax1.set_title('Scatter: $x$ versus $y$')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
 
ax2.hist(
    data, bins=np.arange(data.min(), data.max()),
    label=('x', 'y')
)
 
ax2.legend(loc=(0.65, 0.8))
ax2.set_title('Frequencies of $x$ and $y$')
ax2.yaxis.tick_right()
 
plt.show()
