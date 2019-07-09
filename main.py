#!/usr/bin/python3

import sys


def addition(x, y):

    result = float(x) + float(y)
    return(result)


def subtraction(x, y):
    result = x - y
    return(result)


def multiplication(x, y):
    result = x * y
    return(result)


def division(x, y):
    result = x / y
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
    else:
        print("This function is not supported!")
