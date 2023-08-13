# print('Hello World!\nI am Adebisi Abdussamad\nI am learn Python')
# print('Hello' + ' ' + 'Adebisi')

# print('Hello ' + input('What is your name?') + '!')

# coding challenge 1.3
# print(len(input('What is your name? ')))
# len() function counts the numbers of character in a string

# name = 'Adebisi'
# print(name)

# name = 'Abdussamad'
# print(name)

# name = input('What is your name? ')
# length = len(name)
# print(length)

# CODE CHALLENGE 01
# print('Welcome to the Band Name Generator.')
# city = input("What's name of the city you grew up in?\n")
# pet = input("What's your pet's name?\n")
# band_name = 'Your band name could be ' + city + " " + pet
# print(band_name)

# DATA TYPES

# print('Hello'[4])

# print(123_878 + 456)

# Interactive Coding 2.1
# type_num = (input('Type a two digit number: '))
# type_num_result = int(type_num[0]) + int(type_num[1])
# print(type_num_result)

# print(3 * 3 + 3 / 3 - 3)

# Interactive Coding 2.2
# height = input('enter your height in m: ')
# weight = input('enter your weight in kg: ')
#
# BMI = int(weight) / float(height) ** 2
# print(int(BMI))

#  round() -> it used to round up an inter/floating number to a whole number
# print(round(8 / 3, 2))
# print(round(8 // 3))
# the 2 after 3 signifies the number of place it should be rounded up to
# if you // to divide then the result will be a whole number cutting the decimal part
# result = 4 / 2
# result /= 2
# print(result)
# height = 1.8
# isWinning = True
# print(f'your result is {result}, your height is {height}, you are winning is {isWinning}')

# Interactive Coding 2.3
# age = input('what is your current age? ')
# age_left = 90 - int(age)
# age_left_in_days = age_left * 365
# age_left_in_weeks = age_left * 52
# age_left_in_month = age_left * 12
# print(age_left_in_month)
# print(f'You have {age_left_in_days} days, {age_left_in_weeks} weeks, {age_left_in_month} months left.')

# CODE CHALLENGE 2
# print('Welcome to the tip calculator.')
# total_bill = float(input('What was the total bill? $'))

# tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))

# tip = (tip_percentage / 100) * total_bill
# split_bill = int(input('How many people to split the bill? '))
# total_bill_for_each = (total_bill + tip) / split_bill
# print(f'Each person should pay: {round(total_bill_for_each, 2)}')

# CONDITIONAL STATEMENTS
# print('Welcome to the rollercoaster!')
# height = int(input('What is your height in cm? '))


# if height == 120:
#     print('You can ride the rollercoaster!')
# else:
#     print('Sorry, you have to grow taller before you can ride.')

# Interactive Coding 3.1
# number = int(input('Which number do you want to check? '))
# if number % 2 == 0:
#     print("This is a even number.")
# else:
#     print("This is an odd number.")

# NESTED IF/ELSE STATEMENT
# print('Welcome to the rollercoaster!')
# height = int(input('What is your height in cm? '))

# if height == 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is your age? '))
#     if age < 12:
#         print('Please pay $5.')
#     elif age <= 18:
#         print('Please pay $7.')
#     else:
#         print('Please pay $12.')
# else:

#     print('Sorry, you have to grow taller before you can ride.')

# Interactive Coding 3.1
# height = float(input('enter your height in m: '))
# weight = float(input('enter your weight in kg: '))

# BMI = round(weight / height ** 2)
# if BMI < 18.5:
#     print(f'Your BMI is {BMI}, you are underweight.')
# elif BMI < 25:
#     print(f'Your BMI is {BMI}, you have a normal weight.')
# elif BMI < 30:
#     print(f'Your BMI is {BMI}, you are slightly overweight')
# elif BMI < 35:
#     print(f'Your BMI is {BMI}, you are obese.')
# else:
#     print(f'Your BMI is {BMI}, you are clinically obese.')

# Interactive Coding 3.2
# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('leap year.')
#         else:
#             print('not leap year.')
#     else:
#         print('leap year.')
# else:
#     print('Not leap year')

# Multiple conditions
# print('Welcome to the rollercoaster!')
# height = int(input('What is your height in cm? '))
# bill = 0

# if height > 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is your age? '))
#     if age < 12:
#         bill = 5
#         print('Child ticket are $5.')
#     elif age <= 18:
#         bill = 7
#         print('Youth ticket are $7.')
#     else:
#         bill = 12
#         print('Adult ticket are $12.')
#     wants_photos = input('Do you want a photo taken? Y or N. ')
#     if wants_photos == 'Y':
#         bill += 3
#     print(f'Your final bill is ${bill}')


# else:
#     print('Sorry, you have to grow taller before you can ride.')

# Interactive Coding 3.3
# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# bill = 0
# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# else:
#     bill += 25
# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == 'Y':
#     bill += 1
# print(f'Your final bill is: ${bill}')

# Logical Operators
# and
# or
# not
# print('Welcome to the rollercoaster!')
# height = int(input('What is your height in cm? '))
# bill = 0
#
# if height > 120:
#     print('You can ride the rollercoaster!')
#     age = int(input('What is your age? '))
#     if age < 12:
#         bill = 5
#         print('Child ticket are $5.')
#     elif age <= 18:
#         bill = 7
#         print('Youth ticket are $7.')
#     elif 45 <= age <= 48:
#         bill = 0
#         print('Midlife crises ticket is $0.')
#
#     else:
#         bill = 12
#         print('Adult ticket are $12.')
#     wants_photos = input('Do you want a photo taken? Y or N. ')
#     if wants_photos == 'Y':
#         bill += 3
#     print(f'Your final bill is ${bill}')
# else:
#     print('Sorry, you have to grow taller before you can ride.')

# Interactive Coding 3.5

print('Welcome to the Love Calculator!')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

name1_in_lowercase = name1.lower()
name2_in_lowercase = name2.lower()

count_T_in_name1 = name1_in_lowercase.count('t')
count_R_in_name1 = name1_in_lowercase.count('r')
count_U_in_name1 = name1_in_lowercase.count('u')
count_E_in_name1 = name1_in_lowercase.count('e')
count_L_in_name1 = name1_in_lowercase.count('l')
count_O_in_name1 = name1_in_lowercase.count('o')
count_V_in_name1 = name1_in_lowercase.count('v')
count_T_in_name2 = name2_in_lowercase.count('t')
count_R_in_name2 = name2_in_lowercase.count('r')
count_U_in_name2 = name2_in_lowercase.count('u')
count_E_in_name2 = name2_in_lowercase.count('e')
count_L_in_name2 = name2_in_lowercase.count('l')
count_O_in_name2 = name2_in_lowercase.count('o')
count_V_in_name2 = name2_in_lowercase.count('v')

total_for_TRUE_in_name1 = (count_T_in_name1 + count_R_in_name1 + count_U_in_name1 + count_E_in_name1)
total_for_LOVE_in_name1 = (count_L_in_name1 + count_O_in_name1 + count_V_in_name1 + count_E_in_name1)
total_for_TRUE_in_name2 = (count_T_in_name2 + count_R_in_name2 + count_U_in_name2 + count_E_in_name2)
total_for_LOVE_in_name2 = (count_L_in_name2 + count_O_in_name2 + count_V_in_name2 + count_E_in_name2)

total_for_TRUE = total_for_TRUE_in_name1 + total_for_TRUE_in_name2
total_for_LOVE = total_for_LOVE_in_name1 + total_for_LOVE_in_name2

total_in_string = str(total_for_TRUE) + str(total_for_LOVE)

love_score = int(total_in_string)
if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos')
elif love_score > 40 and love_score < 50:
    print(f'Your score is {love_score}, you are alright together')
else:
    print(f'Your score is {love_score}')
