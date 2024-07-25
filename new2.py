def add(*args):
    return sum(args)


def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


def divide(*args):
    result = args[0]
    for num in args[1:]:
        result /= num
    return result


def square(*args):
    result = []
    for num in args:
        result.append(num**2)
    return result


def square_root(*args):
    result = []
    for num in args:
        from math import sqrt

        result.append(sqrt(num))
    return result


def sine_angle(*args):
    result = []
    for num in args:
        from math import sin, radians

        angle_radian = radians(num)
        result.append(sin(angle_radian))
        return result

    return result


def cosine_angle(*args):
    result = []
    for num in args:
        from math import cos, radians

        angle_radian = radians(num)
        result.append(cos(angle_radian))
        return result


while True:
    n = int(input("enter the number of inputs"))
    inputs = []
    for num in range(n):
        user_input = int(input("enter the value:"))
        inputs.append(user_input)
        print("you entered:", inputs)
    print(
        """Name Of Operations
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Division
          5. Square of number
          6. Square Root
          7. Sin Angle value
          8. Cosine Angle Value"""
    )

    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")
    if choice == "1":
        result = add(*inputs)
        print("Result of addition:", result)
    elif choice == "2":
        result = subtract(*inputs)
        print("Result of subtraction:", result)
    elif choice == "3":
        result = multiply(*inputs)
        print("Result of multiplication:", result)
    elif choice == "4":
        result = divide(*inputs)
        print("Result of division:", divide(*inputs))
    elif choice == "5":
        result = square(*inputs)
        print("result of square", result)
    elif choice == "6":
        result = square_root(*inputs)
        print("result of square root", result)
    elif choice == "7":
        result = sine_angle(*inputs)
        print("result of sine angle:", result)
    elif choice == '8':
        result = cosine_angle(*inputs)
        print("result of cos angle:", result)
    else:
        print("invalid choice")
    choice = str(input("Do You Want To Continue?" " y for yes n for no:"))
    if choice == "n":
        print("good bye sir")
        break
