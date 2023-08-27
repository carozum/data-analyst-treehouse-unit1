import math


def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than one person is required to split the check")
    return math.ceil(total / number_of_people)


try:
    total_due = float(input("What is the total ?   "))
    number_of_people = int(input("How many people ?   "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("Oh no!, that is not a valid value. Try it again...")
    print(f"({err})")
else:
    print(f"Each person owes {amount_due} euros")
