name = input("Please enter your name:   ")
print(f"Hey {name} !")

number = input("Please enter a number:    ")
try:
    number = int(number)
except ValueError:
    print("You must enter an integer.")
else:
    print(f"The number {number} is ...")

    is_fizz = (number % 3 == 0)
    is_buzz = (number % 5 == 0)

    if is_fizz and is_buzz:
        print("a FizzBuzz number.")
    elif is_fizz:
        print("is a Fizz number.")
    elif is_buzz:
        print("is a Buzz number.")
    else:
        print("is neither a fizzy or a buzzy number.")
