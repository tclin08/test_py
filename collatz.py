#coding=utf-8

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)

        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)

def user():
    try:
        print('Please enter a number')
        num = int(input())
        collatz(num)
    except ValueError:
        print('Enter a valid number')

user()