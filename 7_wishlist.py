books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

# ERROR in this function as the list is changed by the pop() method when the function is called !! books and video games are changed each time the function is called as they are global variables and mutable.


def display_wishlist(display_name, wishes):
    suggested_gift = wishes.pop(0)
    print("======>", suggested_gift, "<======")
    for wish in wishes:
        print("* " + wish)
    print()


# CORRECTION OF THE ERROR making a copy of the list that has a function scope

def display_wishlist(display_name, wishes):
    items = wishes.copy()
    suggested_gift = items.pop(0)
    print("======>", suggested_gift, "<======")
    for item in items:
        print("* " + item)
    print()


# ANOTHER SOLUTION without altering the list passed as an argument

# def display_wishlist(display_name, wishes):
#     print(display_name)
#     print("======>", wishes[0], "<======")
#     for wish in wishes[1:]:
#         print("* " + wish)
#     print()


display_wishlist("video_games", video_games)
display_wishlist("books", books)
display_wishlist("books", books)

# at the function call, parameters are the labels that are given to the arguments which are the value, ie :
# in the function call :
#       display_name = books
#       wishes = books
#       whishes.pop()
# the label only last while the function is running and then is removed. But during that function execution, the label, wishes is referring to the same object, the list of books. That is why when we call pop(0), it changes the object because it is the same object.
print(books)


# about namespaces and scopes
# https://docs.python.org/3/tutorial/classes.html#a-word-about-names-and-objects

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
