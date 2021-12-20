# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function

def hello_name(user_name):
    print(f"hello_{user_name}!")

hello_name("USERNAME")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    n = 1 
    while (n<=100):
        if n % 2 != 0:
            print(n)
        n += 1

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list():
    list = [11, 87, 32, 35, 4]
    list.sort()
    print(list[-1])

max_num_in_list()

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    return a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0)
a_year = [2005, 1992, 2020, 1902]
print(list(map(is_leap_year, a_year)))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers
# MATH UGH min to max, distance
# between the two is no more or less.
# I almost cried when I figured this out
def is_consecutive(a_list):
    if len(a_list) < 1:
        return False
    min_val = min(a_list)
    max_val = max(a_list)
    if max_val - min_val +1 == len(a_list):
        for i in range(len(a_list)):
            if a_list[i] < 0:
                j = -a_list[i] - min_val
            else:
                j = a_list[i] - min_val
                if a_list[j] > 0:
                    a_list[j] = -a_list[j]
                else:
                    return False
        return True
    return False
a_list = [5, 6, 7, 8, 9]
print(is_consecutive(a_list))