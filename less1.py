# Задание 1
# Условие
# Получите строку от пользователя.
# Задача
# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# В девятой строке выведите длину данной строки.

string1 = 'AbraKadabra'
print(string1[2])
print(string1[9:10])
print(string1[:5])
print(string1[:-2])
print(string1[::2])
print(string1[1::2])
print(string1[::-1])
print(string1[-1::-2])
print(len(string1))

# Задание 2
# Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения задачи метод count.

string2 = 'car bike train bus'
word_count = len(string2.split())
print(word_count)

# Задание 3
# Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, то длина первой части должна быть на один символ больше).
# Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.
# При решении этой задачи не стоит пользоваться инструкцией if.

string3 = 'Python is a high-level programming language'
word_count2 = len(string3)
new_str = ''
if len(string3) % 2:
    new_str = (len(string3) // 2)
else:
    new_str = (len(string3 + 1) // 2)

first_part = string3[:new_str]
second_part = string3[new_str:]
new_str2 = second_part + first_part
print(new_str2)

# Задание 5
# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.

# string4 = 'Driving down the highway, we enjoyed the scenic views and the smooth pavement beneath our wheels.'
# first = string4.index('h')
# last = string4.index('h')
#
# if first < last:
#     result = string4[:first] + string4[last + 1]
#     result1 = result.replace('h', '')
#     result2 = result.replace('h', '')

# Задание 6
# Дана строка. Замените в этой строке все цифры 1 на слово one.

string5 = '1 0 1 1 0 0'
mod_string = string5.replace('1', 'one')
print(mod_string)

# Задание 7
# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

string6 = 'Hi there! How are you doing today?'
res = ''
for i , char in enumerate(string6):
    if i % 3 != 0:
        res +=char

print(res)

# Задание 8
# Создайте функцию, которая выдает персональное приветствие.
# Эта функция принимает два параметра: имя и владелец. Используйте условные обозначения, чтобы вернуть нужное сообщение:

def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'

# Задание 9
# Вам нужно написать функцию, которая меняет местами слова в заданной строке.
# Слово также может быть пустой строкой.
string7 = "Hello , World"
def replaсe_words(string7):
    words = string7.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)
    return reversed_string
result = replaсe_words(string7)
print(result)