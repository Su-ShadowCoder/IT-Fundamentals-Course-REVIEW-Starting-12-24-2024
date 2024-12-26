# # # print function
# print(f"Hello world!")
# 2# Always use dubbel quotes- so u can use single quotes in a string like for a sentence
# # integer is a whole number
# # and everthing with a decimal behind the number it becomes a float
# print(f"First line, \nSecond line,")
# print(f"Third line.")

# print(f"First line.")
# print(f"\nThird line.")

# # print(f"""")

# print(f"A =", 3, "helloo!!!")

# three = 3
# my_name = "suda"

# print(f"I am {three} years old, and my name is {my_name}.")

#smol git test.
# second smal test

# PEP 8 Conventions
# indentation's needs to be Consistent
# Limit the code lines to a maximum of 79 characters.
# You can limit the character's by changing the settings in your coding editor.

#Giving function's a different name: 
# different_name  = print
# different_name(f"Hellow world!")

# Variables

# name_var = "Max"
# age_var = 23
# weight_in_kg = 75.5

# print(f"Hello!, My name is {name_var}, I'm {age_var} years old.\nand I weight {weight_in_kg} Kg.")

# Do not use specifiek keywords that act as functions in your variable name. according to the pep8 conventions.

# If u decide to make a var name, try to use 3 word names with underscore connecting it. as spaces would the editor consider it as every word is it's own independent var. so like this name_var or avg_data_age.

# Naming variable's exercise
# rotten_fruits_numb = # amount of rotten fruits.
# prime_numb_lst = # the list of prime numbers.
# math_exam_scores = # the list of mathematix exam scores.

# Exercise
# January = March = May = July = August = October = December = 31
# April = June = September = November = 30
# February = 28

# print(January, February, March, April, May, June, July, August, September, October, November, December)

# When there is no value asigned to a variable or you dont know for now, you could asign it to be temporarly or permananently "None" value without the quotations marks. depending on the situation.

#  Paused at 01:46 min, python 2 zoom lesson video. 

# Basic Data Types
# String 
# Integer
# Float
# Boolean

# email_adres = "alfred@clarusway.com"
# id_numb = "632"
# secret_course_paswrd = "It's early"

# print(f"The e-mail adres is: {email_adres}, with the id number of {id_numb}, and the secret password is:{secret_course_paswrd}.")

# str_number = "1923"
# str_sign = "&(*^#$"

# print(str_number)
# print(str_sign)
# print(type(str_number), type(str_sign))

# integer are whole numbers, it could be negative.
# floats has numbers with decimals, usualy its better to store a vulue in whole numbers if there is no decimal.
# 
# Boolean False or True

# prime = 7
# primes =  [3, 7, 11, 13, 23, 101]
# is_prime = prime in primes

# print(is_prime)

# so in this situations it is true that there is prime in primes list, essentialy its asking when you are asking to print, to print if its true that 7 is in the list of primes. and as you can see in the terminal is say true because there is a 7 in the list. and true is thus the boolean value.

# Type conversion
# converting data types.

# you can use these following to convert Datatypes:
# - str() converts to string type.
# - int() converts to integer type.
# - float() converts to floating type.

# able to convert string number into int or float.

# The value of any type in python can be converted to a string. except for exceptions.

# when a float var is converted to a int var ALL the deciamals will be erased of which means anynumber behind the whole number gets erased. 2.36341234534 would become 2, 5.9998877 would become 5.

# and when a int becomes a float it will add one zero of decimal if there is no existing decimal. 5 would become 5.0 and 42 would become 42.0

# you cant add a int and a string togheter or you would get a error, even if the string consist only of whole numbers. so first convert the string to int, before you do a mathmatical handeling with a integer(int)

#Danzo. for today

# Arithmetic Operations
# example: 
# 100 + 45 = 145
# 500 - 65 = 435
# 25 * 4 = 100
# 10 / 2 = 5.0
# 11 // 2 = 5           division where decialmeista
# 5 ** 3 = 125          exponent
# 10 % 3 = 1           remainder
# 16 ** 0.5 =  4    you wouol do scare root base number evertime you do exponent of 0,5 , wortel.


# This is shorter version people prefer to use in Phython.
# x += 3    =    x = x + 3
# x *= 3    =    x = x * 3
# x **= 3   =    x = x ** 3


# x = 6
# x *= 2 
# print(f"{x}")

# print("we are", "\boosting", "our", "\brotherhood")


# Boolean Logic

# and   =  Return True if all expressions are evaluated True, it otherwise returns False

# or    =  returns True if any expressions evaluates to True. otherwise , it returns False

# not   =  it evaluates the expression that follows it as the opposite of the truth. eg. not True means False

# order of priority python takes:
#- not
#- and
#- or

  