"""this program is for a simple calculator which performs basic arithmetic operations like addition, subraction, multiplication, division """

#this funtion is defind to add two numbers

def add(value1,value2):
    sum = value1 + value2
    print("sum of value1 and value2 is:",sum)

#this function is defined to subract two numbers

def sub(value1,value2):
    difference = value1 - value2
    print("subraction of value1 and value2 is:",difference)

#this function is defined to multiply two numbers

def multiply(value1,value2):
    total = value1 * value2
    print("multiplication of value1 and value2 is:",total)  

#this function is defined to divide two numbers

def divide(value1,value2):
    division = value1 / value2
    print("division of value1 and value2 is:",division)

#A Loop is used here to run the code until the user wants to use it
while True:
#now take inputs from the user for values
    value1 = int(input("enter the first number:"))
    value2 = int(input("enter the second number:"))

#tell about the operations which can be performed

    print("please select operation:\n" "1.addition\n" "2.subraction\n"  "3.multiplication\n" "4.division\n" "5.quit")

#take input from the user that which operation should be performed via 1, 2, 3, 4, 5 numbers

    operator = int(input("enter the operation to  perform via 1,2,3,4,5:"))
    if operator == 5:
        print("good bye")
        break

#using conditions to perform according to the input given to the operator

    if operator == 1:
     add(value1,value2)
    elif operator == 2:
     sub(value1,value2)
    elif operator == 3:
     multiply(value1,value2)
    elif operator == 4:
     divide(value1,value2)
    else:
     print("wrong input")