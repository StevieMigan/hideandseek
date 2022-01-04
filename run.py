from random import randint

scores = {"computer": 0, "player": 0}

print("""**********************************************************************
Hello! Welcome to Hide & Seek!
Hide & Seek is a logic-based game built entirely in Python.
You have 5 team members that are hidden randomly on your grid...
Can you find the other team's 5 players before they find yours?
KEY
x = Sorry, Nobody is hiding there!
o = Bingo! You found one of my team!
**********************************************************************""")

player_name = input("Firstly, what is your name?: \n")
print("Hi " + player_name + ", let's play Hide & Seek!\n")
print(player_name,"- Here's where your team are hiding!\n")


def create_grid_p1():
    grid = []
    for row in range(5):
        print(" - " * 5)

create_grid_p1()

print("\n")
print("Player two - Where are they hiding? ;)")
print("\n")
def create_grid_p2():
    grid = []
    for row in range(5):
        print(" - " * 5)

create_grid_p2()

