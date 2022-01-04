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

print("   0  1  2  3  4  ")
for i in range(5):
    print(i, " - " * 5)

print("\n")
print("Player two - Where are they hiding? ;)")
print("\n")

print("   0  1  2  3  4  ")
for i in range(5):
    print(i, " - " * 5)



