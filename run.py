import random

print("**********************************************************************")
print("Hello! Welcome to Hide & Seek!")
print("Hide & Seek is a logic-based game built entirely in Python.")
print("You have 5 team members that are hidden randomly on your grid...")
print("Can you find the other team's 5 players before they find yours?")
print("KEY")
print("x = Sorry, Nobody is hiding there!")
print("o = Bingo! You found one of my team!")
print("**********************************************************************")

player_name = input("Firstly, what is your name?: ")
print("\n")
print("Hi " + player_name + ", let's play Hide & Seek!")
print("\n")

print(player_name,"- Here's where your team are hiding!")
print("\n")
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