"""this code is for a calculator which perform specified operation on a variable no of inputs."""


def add(*args):
    """this function add all the inputs"""
    return sum(args)


def subtract(*args):
    """subtract all subsequent inputs from the first input."""
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def multiply(*args):
    "Multiply all inputs."
    result = 1
    for num in args:
        result *= num
    return result


def divide(*args):
    """Divide the first input by all subsequent inputs"""
    result = args[0]
    for num in args[1:]:
        result /= num
    return result


def square(*args):
    """Returns the square of the inputs."""
    result = []
    for num in args:
        result.append(num**2)
    return result


def square_root(*args):
    """Returns the square root of the inputs."""
    result = []
    for num in args:
        from math import sqrt

        result.append(sqrt(num))
    return result


def sine_angle(*args):
    """Returns the sine of the input (angles in radian)"""
    result = []
    for num in args:
        from math import sin, radians

        angle_radian = radians(num)
        result.append(sin(angle_radian))
        return result

    return result


def cosine_angle(*args):
    """Returns the cosine of the input(angles in radian)"""
    result = []
    for num in args:
        from math import cos, radians

        angle_radian = radians(num)
        result.append(cos(angle_radian))
        return result


# start a infinite loop until it breaks.
while True:
    # take input from the user
    n = int(input("enter the number of inputs: "))
    # initialize a empty list.
    inputs = []
    # start a new loop upto range n
    for num in range(n):
        user_input = int(input("enter the value:"))
        inputs.append(user_input)
        print("you entered:", inputs)
        # display all the operations which can be performed with numbers.
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
    # tae input numbers from the user.
    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")
    # sum all the inputs.
    if choice == "1":
        result = add(*inputs)
        print("Result of addition:", result)
    # subtract each subsequent input from the first one.
    elif choice == "2":
        result = subtract(*inputs)
        print("Result of subtraction:", result)
    # multiply all inputs.
    elif choice == "3":
        result = multiply(*inputs)
        print("Result of multiplication:", result)
    # divide the first input by each subsequent.
    elif choice == "4":
        result = divide(*inputs)
        print("Result of division:", divide(*inputs))
    # square all inputs.
    elif choice == "5":
        result = square(*inputs)
        print("result of square", result)
    # square root of each inputs.
    elif choice == "6":
        result = square_root(*inputs)
        print("result of square root", result)
    # sine  of each input.
    elif choice == "7":
        result = sine_angle(*inputs)
        print("result of sine angle:", result)
    # cos of each input.
    elif choice == "8":
        result = cosine_angle(*inputs)
        print("result of cos angle:", result)
    # if there is invalid choice.
    else:
        print("invalid choice")
    choice = str(input("Do You Want To Continue?" " y for yes n for no:"))
    if choice == "n":
        print("good bye")
        break
