# ******************* TO DO *******************

# As a user, I should be shown the number of tickets left remaining, so I can understand the importance of buying now

# As a user, I should have a personalized experience so that I feel welcomed by the brand

# As a user, I should be able to request a certain amount of tickets and be told the total cost, so that I can determine if I want to purchase the tickets.

# As a user, I should have errors reported in a user friendly manner.

# As a user, I should be able to confirm my order so that I do not accidentally purchase more tickets than intended.

# As a user, I should not be offered tickets if there aren't any available

# As an owner, I should receive a service charge so that I can pay other to maintain the software.

# ******************* BACKLOG *******************

# As a user, I should be able to purchase using credit cards and bitcoins. -> that is out of our scope right now.

# ******************* APP *******************

TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100
print(f"There are {tickets_remaining} tickets remaining")

"""
function calculate price of purchase
@param {int} number of tickets
@return {int} price to pay
"""


def calculate_price(num):
    return (num * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining > 0:

    name = input("What is your name ?   ")
    number_tickets = input(
        f"Hey { name}, how many tickets do you want to buy?  ")

    try:
        number_tickets = int(number_tickets)
        if number_tickets > tickets_remaining:
            raise ValueError(
                f"There are only {tickets_remaining} tickets remaining")
        if number_tickets < 1:
            raise ValueError("You must select at least one(1) ticket")
    except ValueError as err:
        if "base 10" in str(err):
            print("Houston, we have a problem. Please be sure to use a number.")
            print("*" * 50)
        else:
            print(f"Oh we ran into an issue.{err}. Please try again")
            print("*" * 50)
    else:

        amount_due = calculate_price(number_tickets)
        print(f"The total price is {amount_due} euros.")

        should_proceed = input(
            "Do you want to confirm you purchase ? Y/N   ")
        if should_proceed.lower() == "y":
            tickets_remaining -= number_tickets
            # TODO: Gather credit card information and process it.
            print("SOLD !")
            print("*" * 50)
            print(f"There are {tickets_remaining} tickets remaining")
            print("*" * 50)
        else:
            print(f"Thank you anyways, {name}.")

print("Sorry, all the tickets are all sold out !! :(")
