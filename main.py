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
height = input('enter your height in m: ')
weight = input('enter your weight in kg: ')

BMI = int(weight) / float(height) ** 2
if BMI < 18.5:
    print(f'You weigh {round(BMI, 2)},\nYou are underweight.')
elif BMI > 18.5:
    print(f'You weigh {round(BMI, 2)},\nYou have a normal weight.')
elif BMI > 25:
    print(f'You weigh {round(BMI, 2)},\nYou are overweight')
elif BMI > 30:
    print(f'You weigh {round(BMI, 2)},\nYou are obese.')
else:
    print(f'You weigh {round(BMI, 2)},\nYou are clinically Obese.')