#!/usr/bin/python3

import sys


def addition(x, y):

    result = float(x) + float(y)
    return(result)


def subtraction(x, y):
    result = float(x) - float(y)
    return(result)


def multiplication(x, y):
    result = float(x) * float(y)
    return(result)


def division(x, y):
    result = float(x) / float(y)
    return(result)

########################################################


numOfArgs = len(sys.argv)

# print( "Number of Arguments: {}".format( numOfArgs ) )
# print( "Arguments List: '{}'".format( sys.argv ) )

if numOfArgs == 1:
    print("Please select a function")
    exit(0)
else:
    fc = sys.argv[1]
    # print( "The function is {}".format( fc ) )

    if fc == "add":
        if numOfArgs == 2:
            print("There are no numbers to add!")
        else:
            result = 0
            for n in sys.argv[2:]:
                result = addition(result, n)
            print(result)
    elif fc == "sub":
        if numOfArgs == 2:
            print("There are no numbers to sub!")
        elif numOfArgs == 4:
            result = subtraction(sys.argv[2], sys.argv[3])
            print(result)
        else:
            print("Please provide two numbers")
    elif fc == "mul":
        if numOfArgs == 2:
            print("There are no numbers to mul!")
        else:
            result = 1
            for n in sys.argv[2:]:
                result = multiplication(result, n)
            print(result)
    elif fc == "div":
        if numOfArgs == 2:
            print("There are no numbers to div!")
        elif numOfArgs == 4:
            if int(sys.argv[3]) != 0:
                result = division(sys.argv[2], sys.argv[3])
                print(result)
            else:
                print("Division by zero is not allowed!")
        else:
            print("Please provide two numbers")
    else:
        print("This function is not supported!")
