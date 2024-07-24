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
def get_input():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    return numbers
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
        
choice = input("Enter your choice (1/2/3/4): ")
nums = get_input()

if choice == '1':
    print("Result of addition:", add(*nums))
elif choice == '2':
    print("Result of subtraction:", subtract(*nums))
elif choice == '3':
    print("Result of multiplication:", multiply(*nums))
elif choice == '4':
    print("Result of division:", divide(*nums))
else:
    print("invalid choice")
