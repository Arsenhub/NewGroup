import random

"""IF, ELIF, ELSE"""

# 1. Enter your name, then find the sum of the ASCII values of the letters in your name. If that number is larger than
# 500, print "I've got a great name!", and "I've got a fancy name!" otherwise.
# Ներմուծեք ձեր անունը և գտեք անվան տառերի ASCII արժեքների գումարը։ Եթե թիվը մեծ է 500-ից, տպել "I've got a great
# name!", իսկ հակառակ դեպքում՝ "I've got a fancy name!"։

name = 'Arsen'
n = (ord('A'), ord('r'), ord('s'), ord('e'), ord('n'))
s = sum(n)
if s >= 500:
    print('I\'ve got a great name!')
else:
    print('I\'ve got a fancy name!')

name = input('Enter your name: ')
total = 0

for char in name:
    total += ord(char)
print(total)
if total > 500:
    print('I\'ve got a great name!')
else:
    print('I\'ve got a fancy name!')

print('-' * 20)

# 2. Ask the user for a movie title. If the title starts with a capital letter, print "Great title!", otherwise print
# "Titles start with capital letters...". If the input starts with a special character [!, @, #, $, %, ^, &], print "I
# doubt that this is a title.".
# Պահանջել ներմուծել ֆիլմի վերնագիր։ Եթե վերնագիրը սկսվում է մեծատառով, տպել "Great title!", հակառակ դեպքում տպել
# "Titles start with capital letters..."։ Եթե ներմուծվածը սկսվում է [!, @, #, $, %, ^, &] նշաններով, տպել "I doubt that
# this is a title."․

user = input('Enter movie title: ')
if user[0].isupper():
    print('Great title!')
elif user.startswith(('!', '@', '#', '$', '%', '^', '&')):
    print('I doubt that this is a title.')
else:
    print('Titles start with capital letters...')

print('-' * 20)

# 3. Ask the user to input his/her age. If the user is older than 18, than tell them they're eligible to vote. If they
# are younger than 18, tell them how many years do they have to wait.
# Հարցրեք օգտատիրոջ տարիքը։ Եթե նա 18 տարեկանից մեծ է, նրան տեղյակ պահեք, որ կարող է քվեարկել։ Հակառակ դեպքում ասեք, թե
# քանի տարուց նա կկարողանա դա անել։

user = int(input('Please enter your age: '))
if user >= 18:
    print('You\'re eligible to vote')
else:
    print(f'you should wait {18 - user} years to have right to vote')

print('-' * 20)

# 4. Write a program that will tell us whether a given year is a leap year or not.
# Գրել ծրագիր, որը կտեղեկացնի, թե տրված տարին նահանջ է, թե ոչ։

year = int(input('Enter Year: '))
if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
    print("Given Year is a leap Year")
else:
    print("Given Year is not a leap Year")
# Google եմ արել

print('-' * 20)

# 5. Using 'random' module, generate a random number between -1000 and 1000. If the number is positive, print positive.
# If it's negative, print negative along with the absolute value of the number.
# Օգտագործելով random գրադարանը, գեներացնել [-1000,1000]-ը տիրույթում պատահական թիվ։ Եթե թիվը դրական է, տպել positive.
# Հակառակ դեպքում տպել negative և այդ թվի բացարձակ արժեքը։

# import random
r_num = random.randint(-1000, 1000)
if r_num > 0:
    print('positive')
elif r_num == 0:
    print(f'{r_num} ')
else:
    print(f'{r_num} is negative')

"""Bonus"""

# 8. Given a string, print a string where for every character in the original, there are two characters.
# Տրված է սթրինգ։ Տպեք նոր սթրինգ, որը կպարունակի օրիգինալ սթրինգի բոլոր տառերը կրկնապատկված։

# Օրինակ, եթե ունենք հետևյալ սթրինգը՝ Monty, պետք է ստանանք MMoonnttyy

string = input('Enter string: ')
char = " "
for i in string:
    char = char + i + i
print(char)

string = 'Monty'
result = ' '

for char in string:
    result += 2 * char
print(result)


# 9. Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So
# "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

s = 'xxcaazz'
s1 = 'xxbaaz'

for i in range(len(s)):
    print(s[i:i + 2])
# mnacac@ nayel heto


# 10. Reverse a string without the use of indexation (e.g. [::-1]).
# Շրջել սթրինգը առանց գործածելու str[::-1]

string = input('Enter string: ')
char = 0
for i in string:
    char += 1

b = ''
for i in string:
    b += a[char-1]
    char -= 1
print(b)

# version_2
string = 'Monty'
result = ' '
for i in range(len(string) -1, -1, -1):
    result += string[i]
print(result)
