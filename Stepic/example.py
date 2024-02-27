'''
Created on 4 июл. 2022 г.

@author: kiril

'''
'''
from _ast import Add
from pickle import TRUE
from asyncio.tasks import sleep
from pip._vendor.pyparsing.core import Forward
'''

'''
p = [x ** 3 for x in range(40)]
pw = set()
for a in range(1, 40):
    for b in range(1, 40):
        for c in range(1, 40):
            for d in range(1, 40):
                s_1 = p[a] + p[b]
                s_2 = p[c] + p[d]
                
                if s_1 == s_2 and a != c and a != d and b != c and b != d:
                    print(a, b, c, d, s_1)
                    pw.add(s_1)
            
print(s_1)
            
p = [x ** 5 for x in range(151)]
pw = set(p)
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                s = p[a] + p[b] + p[c] + p[d]
                if s in pw:
                    print(a, b, c, d, p.index(s))
                    print(a + b + c + d + p.index(s))
                    

'''

''' 
def is_valid(s):
    if s.isdigit() == True and 1 <= int(s) <= 100:
        return True
    else:
        return False

from random import *

n = randrange(1, 101)
print('Добро пожаловать в числовую угадайку, попробуйте угадать ... ')

while True:
    s = input()
    if is_valid(s) == True:
        number = int(s)
        if number == n:
            print('Вы угадали, поздравляем!')
            break
        elif number < n:
            print('Ваше число меньше загаданного, попробуйте еще разок ... ')
        elif number > n:
            print('Ваше число больше загаданного, попробуйте еще разок ... ')
    else:
        print('Попробуй ввести число от 1 до 100 :)') 
'''

'''
from random import * 

l = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай', 
     'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет',
     'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет',
     'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
     'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

while True:
    s = input()
    print(choice(l))
    print()
    print('Выхотите задать ещё вопрос?')
    if input() == 'Yes':
        continue
    else:
        break
'''

'''
from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

print('Введите количество генерируемых паролей ... ')
n = int(input())

print('Введите длинну одного пароля ... ')
lens = int(input())

print('Включать ли цифры 0123456789 в пароль?')
if input() == 'Yes':
    flag_digit = True
else:
    flag_digit = False
    
print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ в пароль?')
if input() == 'Yes':
    flag_ABC = True
else:
    flag_ABC = False

print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz в пароль?')
if input() == 'Yes':
    flag_abc = True
else:
    flag_abc = False
 
print('Включать ли символы !#$%&*+-=?@^_ в пароль?')
if input() == 'Yes':
    flag_simbol = True
else:
    flag_simbol = False
    
print('Исключать ли неоднозначные символы il1Lo0O из пароля?')
if input() == 'Yes':
    flag_exception = True
else:
    flag_exception = False        


chars = digits + lowercase_letters + uppercase_letters + punctuation

password = ''
lens_1 = lens
for _ in range(n):
    while lens_1 >= 0:
        s = choice(chars)
        if (s not in 'il1Lo0O' and flag_exception == True) or (flag_exception != True): 
            if flag_digit == True and s in digits:
                password += s  
            if flag_ABC == True and s in uppercase_letters:
                password += s 
            if flag_abc == True and s in lowercase_letters:
                password += s 
            if flag_simbol == True and s in punctuation:
                password += s
            lens_1 -= 1
    lens_1 = lens
    print(password)
    password = ''
'''

'''
def decode(code, language, s, step):
    
    if code == '0':
        step = step
    else:
        step = -step
    
    for i in range(len(s)):
        if s[i] in ' ,.!\'\"':
            continue
        if language == 'ru':
            number = ord(s[i]) + step
            if 1072 <= number <= 1103 and s[i] == s[i].lower():  
                s = s[:i] + chr(number) + s[i + 1:]
            elif 1040 <= number <= 1071 and s[i] == s[i].upper():
                s = s[:i] + chr(number) + s[i + 1:]
            else:
                if step > 0:
                    s = s[:i] + chr(number - 32) + s[i + 1:]
                else:
                    s = s[:i] + chr(number + 32) + s[i + 1:]
        else:
            number = ord(s[i]) + step
            if 97 <= number <= 122 and s[i] == s[i].lower():  
                s = s[:i] + chr(number) + s[i + 1:]
            elif 65 <= number <= 90 and s[i] == s[i].upper():
                s = s[:i] + chr(number) + s[i + 1:]
            else:
                if step > 0:
                    s = s[:i] + chr(number - 26) + s[i + 1:]
                else:
                    s = s[:i] + chr(number + 26) + s[i + 1:]
    return s
                    
l = [m for m in input().split()]
step = 0

for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j].lower() in 'qwertyuiopasdfghjklzxcvbnm':
            step += 1
    
    print(decode('0', 'en', l[i], step), end=' ')
    step = 0
    
'''

"""
def convert(num_10, ost):
    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    l_ost = []
    while num_10 != 0:
        l_ost.insert(0, l[num_10 % ost])
        num_10 //= ost
    return ''.join(l_ost)    


print('Введите число в десятичной системе исчеления ... ')
num_10 = int(input())
print('Введите число в систему которого хотите перевести введённое число ... (до 16 - ричной)')
ost = int(input())

print(convert(num_10, ost))
'''

'''
def get_word(l):
    return choice(l).upper()

def display_human(tr):
    if tr == 6:
        print('-' * 8)
        print('|', '|', sep=' ' * 6)
        print('|', sep=' ' * 6)
        print('|', sep=' ' * 6)
        print('|', sep=' ' * 6)
        print('|', sep=' ' * 6)
        print('-', sep=' ' * 6)
    elif tr == 5:
        print('-' * 8)
        print('|', '|', sep=' ' * 6)
        print('|', '0', sep=' ' * 6)
        print('|', sep=' ' * 6)
        print('|', sep=' ' * 6)
        print('|', sep=' ' * 6)
        print('-', sep=' ' * 6)
    elif tr == 4:
        print('-' * 8)
        print('|', '|', sep=' ' * 6)
        print('|', '0', sep=' ' * 6)
        print('|', '|', sep=' ' * 6)
        print('|', '|', sep=' ' * 6)
        print('|', sep=' ' * 6)
        print('-', sep=' ' * 6)
    elif tr == 3:
        print('-' * 8)
        print('|', '|', sep=' ' * 6)
        print('|', '0', sep=' ' * 6)
        print('|', '\\\\|', sep=' ' * 5)
        print('|', '|', sep=' ' * 6)
        print('|', sep=' ' * 6)
        print('-', sep=' ' * 6)
    elif tr == 2:
        print('-' * 8)
        print('|', '|', sep=' ' * 6)
        print('|', '0', sep=' ' * 6)
        print('|', '\\\\|/', sep=' ' * 5)
        print('|', '|', sep=' ' * 6)
        print('|', sep=' ' * 6)
        print('-', sep=' ' * 6)
    elif tr == 1:
        print('-' * 8)
        print('|', '|', sep=' ' * 6)
        print('|', '0', sep=' ' * 6)
        print('|', '\\\\|/', sep=' ' * 5)
        print('|', '|', sep=' ' * 6)
        print('|', '/', sep=' ' * 5)
        print('-', sep=' ' * 6)
    elif tr == 0:
        print('-' * 8)
        print('|', '|', sep=' ' * 6)
        print('|', '0', sep=' ' * 6)
        print('|', '\\\\|/', sep=' ' * 5)
        print('|', '|', sep=' ' * 6)
        print('|', '/ \\\\', sep=' ' * 5)
        print('-', sep=' ' * 6)

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    print('Давай сыграем ... ')
    
    letters = list(word.upper())
    guessed_letters = list('*' * len(word))
    tries = 6
 
    
    display_human(tries)
    print('Тебе нужно отгадать слов!')
    print(''.join(guessed_letters))
    
    while tries != 0:
        print('У тебя осталось', tries, 'попыток. Удачи!')
        print('Введи букву')
        let = input().upper()
        if let in guessed_letters:
            print('Ты её уже отгадал. Попробуй ещё.')
        elif not ('А' <= let <= 'Я'):
            print('Все слова на русском. Я в тебя верю ты справишься')
        elif let == word.upper():
            print('Ты справился! Правильное слово!', word.upper())
            break
        elif len(let) > 1 or len(let) == 0:
            print('Одна буква или всё слово целиком по другому никак!')
            print('Прощаю тебя, пробуй ещё.')
        elif let in letters:
            while let in letters:
                guessed_letters[letters.index(let)] = letters[letters.index(let)]
                letters[letters.index(let)] = '*'
            
            if '*' not in guessed_letters:
                print('Да, ты угадал слово -', ''.join(guessed_letters))
                break  
            else:
                display_human(tries)
                print(''.join(guessed_letters))
        else:
            tries -= 1
            
            display_human(tries)
            print(''.join(guessed_letters))
    else:
        print('Попытки закончились. Правильный ответ -', word)
             
    #print()
    #print(display_hangman(tries))
    
    
    


from random import *

l = ['Астронавт', 'Боль', 'Кошмар','Улица' ,'Персик' ,'Карантин' ,'Угол' ,'Смех' ,'Выбор' ,'Пижама' , 'Снеговик']

while True:
    play(get_word(l))
    print('Хочешь сыграть ещё? Если да, то введи - yes')
    s = input()
    if s.capitalize() != 'Yes':
        break
"""

'''
n = int(input())
m = int(input())

l = [i for i in range(1, n + 1)]
i = 0
ans = 0

while i != n:
    i += 1
    if i == 1:
        ans = 1
    else:
        ans = 1 + (ans + m - 1) % i 

print(ans)
'''
'''
n = int(input())
l = [int(input()) for _ in range(n)]
num = int(input())

counter = 0

for i in range(n):
    if num % l[i] == 0 and l[i] != 1:
        counter += 1
    elif 1 in l and l[i] == num:
        counter += 2
    
if counter >= 2:
    print('ДА')
else:
    print('НЕТ')
'''

'''
S = input()
counter_1 = 0
counter_2 = 0

for i in range(len(S) - 1):
    if S[i] == S[i + 1] and S[i] == 'Р':
        counter_1 += 1
    if S[i] != S[i + 1]:
        counter_1 = 0
    if counter_1 > counter_2:
        counter_2 = counter_1 
                  
print(counter_2 + 1)
'''

'''
n = int(input())
fridge = [input() for _ in range(n)]

example = list('anton')
ans = []

for i in range(n):
    for j in range(len(example)):
        if fridge[i].find(example[j]) != -1:
            fridge[i] = fridge[i][fridge[i].find(example[j]) + 1 :]
            continue
        else:
            break
    else:
        ans.append(i + 1)
        
print(*ans)
'''

'''
n = int(input())
row = []
l = []

for i in range(n):
    for j in range(1, n + 1):
        row.append(j)
    l.append(row)
    row.clear()    

for i in range(len(l)):
    print(l[i])
'''

'''
l = input().split()
l_sort = []
sort = []

while l != []:
    one = l[0]
    while one == l[0]:
        sort.append(l.pop(l.index(one)))
        if l == []:
            break
    l_sort.append(sort.copy())
    sort.clear()
    
print(l_sort)
'''
'''
def chunked(s, n):
    l = []
    for i in range(len(s)):
        if i + n <= len(s):
            l.append(s[i : i + n])
        else:
            break
        
    return l

s = input().split()
l = [[]]

for i in range(1, len(s) + 1):
    l.extend(chunked(s, i))
    
print(l)
'''
'''
n = int(input())
matrix = []
counter = 0

for i in range(n):
    row = [int(m) for m in input().split()]
    matrix.append(row)
    
for i in range(n):
    for j in range(n):
        if sum(matrix[i]) / n > matrix[i][j]:
            counter += 1 
    print(counter)
    counter = 0
'''

'''
n = int(input())
m = int(input())

matrix = []
row = []

for i in range(n):
    for j in range(m):
        row.append(i * j)
    matrix.append(row.copy())
    row.clear()
    
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
'''

'''
n = int(input())

matrix = []
matrix_res = []

for i in range(n):
    row = [int(m) for m in input().split()]
    matrix.append(row.copy())    

row.clear()
for i in range(n):
    for j in range(n):
        row.append(matrix[n - 1 - j][i])
    matrix_res.append(row.copy())
    row.clear()
        
        
for i in range(n):
    for j in range(n):
        print(matrix_res[i][j], end=' ')
    print()
'''
'''
xy = input()

y = '87654321'.index(xy[1])
x = 'abcdefgh'.index(xy[0])

field = [['.'] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if (x - j) ** 2 + (y - i) ** 2 == 5:
            field[i][j] = '*'

for row in field:
    print(*row)
'''
'''
n = int(input())
flag = True
total = 0
diag_1 = 0
diag_2 = 0
matrix = []

for _ in range(n):
    row = [int(m) for m in input().split()]
    matrix.append(row.copy())
    
total_ch = sum(matrix[0])

for i in range(n): 
    if sum(matrix[0]) == total_ch:
        flag = False
        break
    for j in range(n):
        total += matrix[j][i]
    if total == total_ch:
        total = 0
        continue
    else:
        flag = False
        break 
        
for i in range(n): 
    diag_1 += matrix[i][j]
    diag_2 += matrix[i][j]
    
if diag_1 != total_ch or diag_2 != total_ch:
    flag = False
        
        
if flag:
    print('YES')
else:
    print('NO')
'''
'''
n, m = [int(m) for m in input().split()]

matrix = [[0] * m for _ in range(n)]

total = 1
i = 0
j = 0

while i != n and j != m:
    matrix[i][j] = total
    total += 1
    q = i + j
    while True:
        i += 1
        j -= 1
        if j < 0 or i == n:
            break
        matrix[i][j] = total
        total += 1
        
    if q < m - 1:
        i = 0
        j = q + 1
    else:
        i = q - m + 2
        j = m - 1
        
        
for row in matrix:
    print(*row)
'''
'''
n, m = [int(m) for m in input().split()]

matrix = [[0] * m for _ in range(n)]

total = 1
flag_1 = True
flag_2 = False

i = 0
j = 0

while True:
    matrix[i][j] = total
    total += 1
    if flag_1 == True and flag_2 == False:
        j += 1
    elif flag_1 == False and flag_2 == True:
        i += 1
    elif flag_1 == True and flag_2 == True:
        j -= 1
    elif flag_1 == False and flag_2 == False:
        i -= 1
    
    if i == n or j == m or i == -1 or j == -1:  
        if j == m:
            flag_1 = False
            flag_2 = True
            i += 1
            j -= 1
        elif i == n:
            flag_1 = True
            flag_2 = True
            i -= 1
            j -= 1
        elif j == -1:
            flag_1 = False
            flag_2 = False
            i -= 1 
            j += 1
        elif i == -1:
            flag_1 = True
            flag_2 = False
            i += 1
            j += 1
    else:
        if flag_1 == True and flag_2 == False and matrix[i][j] != 0:
            flag_1 = False
            flag_2 = True
            i += 1
            j -= 1
        elif flag_1 == False and flag_2 == True and matrix[i][j] != 0:
            flag_1 = True
            flag_2 = True
            i -= 1
            j -= 1
        elif flag_1 == True and flag_2 == True and matrix[i][j] != 0:
            flag_1 = False
            flag_2 = False
            i -= 1 
            j += 1
        elif flag_1 == False and flag_2 == False and matrix[i][j] != 0:
            flag_1 = True
            flag_2 = False
            i += 1
            j += 1
    if total == n * m + 1:
        break
    
for row in matrix:
    print(*row)            
'''
'''
n, m = [int(m) for m in input().split()]
A = []
B = []
C = []

for _ in range(n):
    row = [int(m) for m in input().split()]
    A.append(row.copy())

s = input()
    
for _ in range(n):
    row = [int(m) for m in input().split()]
    B.append(row.copy())
    
C = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        C[i][j] = A[i][j] + B[i][j]
        
for row in C:
    print(*row)
'''

'''
n = int(input())
matrix = []
flag = True

for i in range(n):
    row = [int(m) for m in input().split()]
    matrix.append(row.copy())
    
check_1 = [i for i in range(1, n + 1)]
check_2 = check_1.copy()
check_3 = check_1.copy()

for i in range(n):
    for j in range(n):
        if matrix[i][j] in check_2:
            del check_2[check_2.index(matrix[i][j])]
        else:
            flag = False
  
        if matrix[j][i] in check_3:
            del check_3[check_3.index(matrix[j][i])]
        else:
            flag = False
    check_2 = check_1.copy()
    check_3 = check_1.copy()
    
if flag:
    print('YES')
else:
    print('NO')
'''

'''
n = int(input())

numbers = set(input())

for _ in range(n - 1):
    numbers.intersection_update(input())

sorted_numbers = sorted([int(m) for m in numbers]) 
    
print(*sorted_numbers)
'''
'''
n = int(input())
m = int(input())

myset = {input() for _ in range(n + m)}

print(n +m - 2 * (n + m - len(myset))
'''
'''
m = int(input())
myset_2 = {input() for _ in range(int(input()))}

for _ in range(m - 1):
    myset_1 = {input() for _ in range(int(input()))}
    myset_2.intersection_update(myset_1)
        
print(*sorted(myset_2), sep = '\n')
'''
"""
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

name_in_users = []

for person in users:
    if person['phone'][len(person['phone']) - 1] == '8':
        name_in_users.append(person['name'])
    
print(*sorted(name_in_users), sep = '\n')    
"""

'''
numbers = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}

num = int(input())
s = ''

while num != 0:
    k = num % 10
    s = numbers(k) + s 
    num //= 10
    
print(s)    
'''
'''
s_1 = input()
s_2 = input()
dict1 = {}
dict2 = {}

for i in range(len(s_1)):
    dict1[s_1[i].lower().strip(':, ;\'\"')] = dict1.get(s_1[i].lower().strip(':, ;\'\"'), 0) + 1 
del dict1['']
    
for i in range(len(s_2)):
    dict2[s_2[i].lower().strip(':, ;\'\"')] = dict2.get(s_2[i].lower().strip(':, ;\'\"'), 0) + 1 
del dict2['']
    
if dict1 == dict2:
    print('YES')
else:
    print('NO')
'''
'''
n = int(input())

dict1 = {}

for _ in range(n):
    value, key = input().split()
    dict1[key.lower()] = (dict1.get(key.lower(), '') + ' ' + value).strip()
    
m = int(input())

for _ in range(m):
    print(dict1.get(input(), 'абонент не найден'))
'''
'''
my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}

for key in my_dict:
  i = 0
  while True:
    if my_dict[key][i] > 20:
      del my_dict[key][i]
      i -= 1
    i += 1  
    if i >= len(my_dict[key]):
        break
'''

'''
def build_query_string(params):    
    s = ''    
    
    for key in sorted(params):       
        s += str(key) + '=' + str(params[key]) + '&'

    return s.strip('&')

dict1 = {'name': 'timur', 'age': 28}

print(build_query_string(dict1))
'''
'''
def merge(values):      # values - это список словарей
    dict1 = {}
    
    for el in values:
        for key in el:
            if dict1.get(key) == None:
                dict1[key] = set()
            dict1[key].add(el[key])
    
    return(dict1)
mda = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]

print(merge(mda))

'''
'''
word = {'execute' : 'X', 'read' : 'R', 'write' : 'W'}

n = int(input())

aval = {}

for _ in range(n):
    cite = input().split()
    aval[cite[0]] = cite[1:]

m = int(input())

for _ in range(m):
    cite = input().split()
    if cite[1] in aval:
        if word[cite[0]] in aval[cite[1]]:
            print('OK')
        else:
            print('Access denied')
    else:
        print('Access denied')
'''
'''
n = int(input())

dict1 = {}

for _ in range(n):
    name, goods, total = input().split() 
    if name not in dict1:
        dict1[name] = dict1.get(name, {goods : int(total)})
    else:
        dict1[name][goods] = dict1[name].get(goods, 0) + int(total)

for name in sorted(dict1):
    print(name + ':')
    for goods, total in sorted(dict1[name].items()):
        print(goods, total)
'''

'''
import random

tickets = set()
ticket = []

while len(tickets) != 100:
    while len(ticket) != 7:
        digit = random.randint(0, 9)
        if digit == 0 and ticket == []:
            continue
        else:
            ticket.append(str(digit))
    tickets.add(tuple(ticket))
    ticket = []

for m in tickets:
  print(*m, sep = '')
'''

'''
import random

l = [random.randrange(76) for _ in range(24)]

matrix = [[0]*5 for _ in range(5)]

for m in matrix:
    for i in range(len(m)):
        el = random.choice(l)
        m[i] = el
        del l[l.index(el)]

for m in matrix:
    for i in range(len(m)):
        print(' '.ljust(3, m))
'''
'''
def generate_password(length):
    import string
    import random
    s = ''
    
    while len(s) != length:
        el = random.choice(string.ascii_letters + string.digits)
        if el not in 'lLiI1oO0':
            s += el              
    return s

def generate_passwords(count, length):
    l = [generate_password(length) for _ in range(count)]
    return l



n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep = '\n')
'''
'''
from fractions import *
from math import *

n = int(input())
l = []

for i in range(1, (n + 1) // 2):
    l.append(Fraction(i, n - i))

ans = 0 
for num in l:
    if (num.numerator + num.denominator) == n and ans < num:
        ans = num

print(ans)
'''
'''
from turtle import *

showturtle()
shape('turtle')

forward(100)
right(60)
forward(100)
left(120)
forward(200)
right(120)
forward(200)

setheading(180)
forward(200)

done()
'''
"""
import turtle

def hexagon(a):
  turtle.showturtle()
  turtle.shape('turtle')
  for _ in range(6):
    turtle.forward(a)
    turtle.right(60)
  turtle.forward(a)
  turtle.left(60)
  


a = int(input())

for i in range(100):
    hexagon(a)

"""
'''
import turtle

def hexagon(a):
  turtle.showturtle()
  turtle.shape('turtle')
  for i in range(4):
    turtle.forward(a)
    if i % 2 == 0:
      turtle.right(60)
    else:
      turtle.right(120)
  turtle.forward(a)
  turtle.left(200)


a = int(input())

for i in range(20):
  hexagon(a)
turtle.done()
'''

# ????????????????????????????????????????????????????????????
'''
import turtle
import math
import random

def fewangle(a, n):
  turtle.speed(0)
  turtle.hideturtle()
  color = random.randrange(256), random.randrange(256), random.randrange(256)
  turtle.fillcolor(color)
  turtle.begin_fill()
  for _ in range(n):
    turtle.forward(a)
    turtle.right(360 / n)
  turtle.end_fill()

  
S = 1000
n = random.randrange(3, 10)
a = ((S * 4 * math.tan(math.radians(180) / n)) / n) ** 0.5
turtle.Screen().colormode(255)

x = 0
y = 0
matrix = [[0] * 5 for _ in range(5)]
turtle.tracer(2, 0)

for _ in range(5):
  for _ in range(5):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    fewangle(a, n)
    x += int(a / math.sin(math.radians(180) / n)) + 10 
    n = random.randrange(3, 10)
    a = ((S * 4 * math.tan(math.radians(180) / n)) / n) ** 0.5 
    #x += int(a / math.sin(math.radians(180) / n))
  y += int(a / math.sin(math.radians(180) / n)) + 10
  x = 0
  
turtle.done()
# ????????????????????????????????????????????????????????????
'''

'''    
import turtle
from math import *
from decimal import *

t = Decimal()
turtle.fillcolor('red')
turtle.begin_fill()
while t != Decimal('6.28'):
  x = 128*sin(t)**3
  y = 8*(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t) - 5)
  t += Decimal('0.01')
  turtle.goto(x, y)
turtle.end_fill()

turtle.done()
'''
'''
def print_products(*args):
    goods = [x for x in args if type(x) == str and x != '']
    for i in range(len(goods)):
        print(str(i + 1) + ')', goods[i])


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
'''
'''
from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

data_1 = sorted(data)
data_2 = filter(lambda city: city[1] > 10000000, data_1)
data_3 = list(filter(lambda city: True if city[2] == 'primary' else False, data_2))
data_4 = reduce(lambda x, y: x + y[0] + ' ', data_3, '')
print(data_4)
'''
'''
from functools import reduce

def evaluate(x, *args):
    args = map(lambda i, n: i * (x ** n), args, range(len(args) - 1, -1, -1))
    result = reduce(lambda i, j: i + j, args) 
    return result
    
cons = list(map(int, input().split()))
x = int(input())

print(evaluate(x, *cons))
'''
'''
n = int(input())

cl =[]
it = []

for i in range(n):
    for j in range(int(input())):
        cl.append(list(map(lambda x: True if x.isdigit() and int(x) == 5 else False, input().split()))[1])
    it.append(any(cl))
    cl = []
    
if all(it):
    print('YES')
else:
    print('NO')
'''
'''
from functools import reduce

def d_10(x):
    l = [int(i) for i in x.split('.')]    
    total = 0 
    for i in range(len(l)):
        total += l[len(l) - 1 - i] * (256 ** i)
    return total 

IP = [input() for i in range(int(input()))]
print(*sorted(IP, key=d_10), sep='\n')
'''

'''
file = open('prices.txt', 'rt', encoding='utf-8')
    
total = 0    
for line in file.readlines():
    l_good = list(map(int, filter(str.isdigit, line.split())))
    total += l_good[0] * l_good[1]

print(total)

file.close()
'''
'''
with open('text.txt', 'rt', encoding='utf-8') as file:
    s = file.readline()
    
    print(s[::-1])
'''
'''
import itertools

def num_filt(s):
    s = list(s)
    l = []
    result = []
    for i in range(len(s)):
        if s[i].isdigit() and i != len(s) - 1:
            l.append(s[i])
            if s[i + 1].isdigit() == False:
                 result.append(int(''.join(l)))
                 l = []
        elif s[i].isdigit() and i == len(s) - 1:
            l.append(s[i]) 
            result.append(int(''.join(l)))
        else:
            continue
    return result
    

with open('nums.txt', 'rt', encoding='utf-8') as file:
    Str_all = file.readlines()
    total = 0
    for i in range(len(Str_all)):
        Str_all[i] = [Str_one for Str_one in Str_all[i].split()]
        Str_all[i] = map(num_filt, Str_all[i])
        Str_all[i] = list(itertools.chain(*Str_all[i]))
        total += sum(Str_all[i])
        
print(total)
'''
'''
with open('file.txt', 'rt', encoding='utf-8') as file:
    lines = file.readlines()
    letters = 0
    words = 0
    
    for line in lines:
        m = line.split()
        for word in m:
            for c in word:
                if c.lower() in 'qwertyuiopasdfghjklzxcvbnm':
                    letters += 1
        words += len(m)
            
    print('Input file contains:')
    print(letters, 'letters')
    print(words, 'words')
    print(len(lines), 'lines')
'''
'''
def read_csv():
    with open('data.csv', 'rt', encoding='utf-8') as data:
        keys = [i.strip() for i in data.readline().split(',')]
        result = []
        for line in data:
            values = [i.strip() for i in line.split(',')]
            result.append(dict(zip(keys, values)))
        return result



read_csv()
'''
'''
with open('input.txt', 'rt', encoding='utf-8') as input_file, open('output.txt', 'w', encoding='utf-8') as output_file:
    file_1 = input_file.readlines()
    for i in range(len(file_1)):
        print(str(i + 1) + ')', file_1[i], end='', file=output_file)
'''

'''
with open('goats.txt', 'rt', encoding='utf-8') as input_file, open('answer.txt', 'w', encoding='utf-8') as output_file:
    result = dict()
    for line in input_file:
        if line.strip() == 'COLOURS':
            flag = True
        elif line.strip() == 'GOATS':
            flag = False
        if flag:
            result[line.strip()] = result.get(line.strip(), 0)
        elif flag == False and line.strip() != 'GOATS':
            result[line.strip()] += 1 
    for key in result:
        if result[key]  * 100  > 7 * sum(result.values()): 
            print(key, end='\n', file=output_file)
'''
'''        
n = int(input())

open('output.txt', 'x', encoding='utf-8')

with open('output.txt', 'r+', encoding='utf-8') as output:
    for _ in range(n):
        with open(input(), 'rt', encoding='utf-8') as file:
            output.seek(0)
            old = [i.strip() for i in output.readlines()]
            output.seek(0)
            new = file.readlines()
            if len(old) > len(new):
                new.extend([''] * (len(old) - len(new)))
            elif len(old) < len(new):
                old.extend([''] * (len(new) - len(old)))            
            output.writelines(list(map(lambda x, y: x + y, old, new)))
'''
'''        
n = int(input())

open('output.txt', 'x', encoding='utf-8')

with open('output.txt', 'a', encoding='utf-8') as output:
    for _ in range(n):
        with open(input(), 'rt', encoding='utf-8') as file:
            for line in file:            
                output.write(line)
'''
'''
with open('logfile.txt', 'r', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as output:
    for line in file:
        name, enter, exit = line.split(',')
        enter = [int(i) for i in enter.split(':')]
        exit = [int(i) for i in exit.split(':')]
        if (exit[0] - enter[0]) * 60 + (exit[1] - enter[1]) >= 60:
            print(name, file=output)
'''
'''
with open('words.txt', 'rt', encoding='utf-8') as file:
    words = file.read().split()
    m = len(max(words, key=len))
    words = filter(lambda word: len(word) == m, words)
    print(*words, sep='\n')
'''
'''
with open('test_1.txt', 'rt', encoding='utf-8') as file:
    print(*[i.strip() for i in file.readlines()][-10::1], sep='\n')
'''
'''
with open('data.txt', 'rt', encoding='utf-8') as file, open('forbidden_words.txt', 'rt', encoding='utf-8') as forbit_file:
    forbit = forbit_file.read().split() 
    data = file.read()
    for word in forbit:
        while word in data.lower():
            pos = data.lower().find(word)
            if pos == 0: 
                data = '*' * len(word) + data[pos + len(word):]
            else:
                data = data[:pos] + '*' * len(word) + data[pos + len(word):]
    print(data)
'''
'''
with open(input(), 'rt', encoding='utf-8') as file:
    line_1 = ''
    l = []
    for line in file:
        if line_1 == '' and 'def ' in line:
            l.append(line[4 : line.find('(')].strip())
        elif 'def ' in line and line_1[0] != '#':
            l.append(line[4 : line.find('(')].strip())
        line_1 = line.strip() 
          
    if l == []: 
        print('Best Programming Team')
    else:
        print(*l, sep='\n')
'''
'''
from mpl_toolkits.mplot3d import axes3d 
import matplotlib.pyplot as plt 
import numpy as np 
 
# Create a range of values for the x- and y-axes 
x = np.arange(-10, 10, 0.1) 
y = np.arange(-10, 10, 0.1) 
 
# Use the meshgrid function to create a grid of x- and y-coordinates 
X, Y = np.meshgrid(x, y) 
 
# Compute the z-coordinates for the hyperbolic paraboloid 
Z = X**2 - Y**2 
 
# Create a 3D axes object 
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
 
# Plot the surface using the x-, y-, and z-coordinates 
ax.plot_surface(X, Y, Z) 
 
# Add labels and a title to the chart 
ax.set_xlabel('x') 
ax.set_ylabel('y') 
ax.set_zlabel('z') 
ax.set_title('Hyperbolic Paraboloid') 
 
# Show the plot 
plt.show()
'''
'''
from mpl_toolkits.mplot3d import axes3d 
import matplotlib.pyplot as plt 
import numpy as np 
 
# Create a range of values for theta and phi 
theta = np.arange(0, 2 * np.pi, 0.01) 
phi = np.arange(0, 2 * np.pi, 0.01) 
 
# Use the meshgrid function to create a grid of theta- and phi-coordinates 
THETA, PHI = np.meshgrid(theta, phi) 
 
# Compute the x-, y-, and z-coordinates for the toroid 
R = 4 
r = 1 
X = (R + r * np.cos(PHI)) * np.cos(THETA) 
Y = (R + r * np.cos(PHI)) * np.sin(THETA) 
Z = r * np.sin(PHI) 
 
# Create a 3D axes object 
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
 
# Plot the surface using the x-, y-, and z-coordinates 
ax.plot_surface(X, Y, Z) 
 
# Add labels and a title to the chart 
ax.set_xlabel('x') 
ax.set_ylabel('y') 
ax.set_zlabel('z') 
ax.set_title('Toroid') 
 
# Show the plot 
plt.show()
'''
'''
import turtle
turtle.speed(0)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()

def sq(a):
    for _ in range(4):
        turtle.forward(a)
        turtle.left(90)

a = 20
b = 20
for _ in range(10):
    sq(a) 
    a += b

turtle.done()
'''

s = ''.join([i for i in input() if i not in '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~1234567890'])

j = 0
k = 0
if len(s) % 2 == 0:
    l = len(s) // 2
else:
    l = len(s) // 2 + 1

for i in range(l):
    if s[i + j] == s[-1 - i - k]:
        continue
    else:
        if j >= 1 or k >= 1:
            print('False')
            break

        if s[i + 1] == s[-1 - i]:
            j += 1
            continue
        else:
            if s[i] == s[-2 - i]:
                k += 1
                continue
            else:
                print('False')
                break

else:
    print('True')

print(s)
