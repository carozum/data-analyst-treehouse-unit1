name = input("What's your name ?   ").capitalize()
answer = input(
    f"{name}, do you understand Python while loops?\n(Enter yes/no)  ")

while answer.lower() != "yes":
    print(
        f"OK, {name}, while loops in Python repeat as long as a certain Boolean condition is met")
    answer = input(
        f"{name}, now do you understand Python while loops?\n(Enter yes/no)  ")

print(
    f"That's great {name}. I'm pleased that you understand while loops now. That was getting repetitive.")
