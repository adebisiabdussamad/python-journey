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

# print('Welcome to the Love Calculator!')
# name1 = input('What is your name? \n')
# name2 = input('What is their name? \n')

# name1_in_lowercase = name1.lower()
# name2_in_lowercase = name2.lower()

# count_T_in_name1 = name1_in_lowercase.count('t')
# count_R_in_name1 = name1_in_lowercase.count('r')
# count_U_in_name1 = name1_in_lowercase.count('u')
# count_E_in_name1 = name1_in_lowercase.count('e')
# count_L_in_name1 = name1_in_lowercase.count('l')
# count_O_in_name1 = name1_in_lowercase.count('o')
# count_V_in_name1 = name1_in_lowercase.count('v')
# count_T_in_name2 = name2_in_lowercase.count('t')
# count_R_in_name2 = name2_in_lowercase.count('r')
# count_U_in_name2 = name2_in_lowercase.count('u')
# count_E_in_name2 = name2_in_lowercase.count('e')
# count_L_in_name2 = name2_in_lowercase.count('l')
# count_O_in_name2 = name2_in_lowercase.count('o')
# count_V_in_name2 = name2_in_lowercase.count('v')

# total_for_TRUE_in_name1 = (count_T_in_name1 + count_R_in_name1 + count_U_in_name1 + count_E_in_name1)
# total_for_LOVE_in_name1 = (count_L_in_name1 + count_O_in_name1 + count_V_in_name1 + count_E_in_name1)
# total_for_TRUE_in_name2 = (count_T_in_name2 + count_R_in_name2 + count_U_in_name2 + count_E_in_name2)
# total_for_LOVE_in_name2 = (count_L_in_name2 + count_O_in_name2 + count_V_in_name2 + count_E_in_name2)

# total_for_TRUE = total_for_TRUE_in_name1 + total_for_TRUE_in_name2
# total_for_LOVE = total_for_LOVE_in_name1 + total_for_LOVE_in_name2

# total_in_string = str(total_for_TRUE) + str(total_for_LOVE)

# love_score = int(total_in_string)
# if love_score < 10 or love_score > 90:
#     print(f'Your score is {love_score}, you go together like coke and mentos')
# elif love_score > 40 and love_score < 50:
#     print(f'Your score is {love_score}, you are alright together')
# else:
#     print(f'Your score is {love_score}')

# Coding Challenge 3
# import random
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
#  ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")

# Write your code below this line 👇
# first_move = input(
#     'You\'re at a crossroad. Where do you want to go? "left" or "right"? ').lower()

# if first_move == 'left':
#     second_move = input(
#         'You come to a lake. Do you want to "swim" or "wait"? ').lower()
#     if second_move == 'wait':
#         third_move = input(
#             'You see three doors - "red", "blue", and "yellow". Which one do you choose? ').lower()
#         if third_move == 'blue':
#             print('Eaten by beasts. Game Over🏴‍☠️')
#         elif third_move == 'red':
#             print('Burned by fire. Game Over🏴‍☠️')
#         elif third_move == 'yellow':
#             print('Congratulations! You found the treasure and won the game!🏆🪙')
#         else:
#             print('Game Over')
#     else:
#         print('You were attacked by a giant trout. Game Over🏴‍☠️')
# else:
#     print('You fell into a hole. Game Over🏴‍☠️')


# RANDOMISATION

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")


# Interactive Coding 4.1
# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇

# random_int = random.randint(0, 1)

# if random_int == 1:
#     print('Heads')
# else:
#     print('Tails')

# LISTS(DATA STRUCTURE)

# states_in_america = [
#     'Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii'
# ]
# states_in_america[1] = 'Lagos'
# states_in_america.append('Karu')
# print(states_in_america)


# Interactive Coding 4.2
# Import the random module here
# import random
# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# random_name = random.randint(1, len(names)-1)
# Write your code below this line 👇
# print(names[random_name])
# print(f'{names[random_name]} is going to buy the meal today!')
# print(names[random_name])


# Interactive Coding 4.3
# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇


if int(position) == 11:
    map[0][0] = 'X'
elif int(position) == 21:
    map[0][1] = 'X'
elif int(position) == 31:
    map[0][2] = 'X'
elif int(position) == 12:
    map[1][0] = 'X'
elif int(position) == 22:
    map[1][1] = 'X'
elif int(position) == 32:
    map[1][2] = 'X'
elif int(position) == 13:
    map[2][0] = 'X'
elif int(position) == 23:
    map[2][1] = 'X'
elif int(position) == 33:
    map[2][2] = 'X'
# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")