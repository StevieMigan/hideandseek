from random import randint

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

print("     0  1  2  3  4  ")

choice = [21,22,23]

coords = 0
for x in range(5):
    row = ""
    for y in range(5):
        marker = " - "
        if coords in choice:
            marker = " X "
        row = row + marker
        coords = coords + 1
    print(x," ",row)








