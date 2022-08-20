import random
from unicodedata import name # imporitng random


 # wellcoming the users 
print('Wellcome to this Decission making animations movie game. Where computer will decide what movie you will watch today!')
  # getting user inputs by making them typing y or n
user = input("Type 'Y' for yes, 'N' for no: ").lower() # .lower() will everything make lowercase

 # if else statement for knowing what the user has typed
if user == 'y':
    print("Okay Let's play this game")
elif user == 'n':
    print('Sorry! To hear that. We will see you again! ')
    quit() # quit is simply gonna quite the programe
else:
    print('Invalid letter. Please ')


 # list of anime
anime = ['Spirited Away (2001)', 'Soul (2020)', 'Zootopia (2016)', 'Inside Out','The Incredibles (2004)', 'Spider-Man: Into the Spider-Verse (2018)']

# getting user input
user_input = input('Type yes to genrate a random move: ').lower()
if user_input == 'yes':
    random_anime = random.choice(anime)
    print(f'Yay! You have got a ranodm movie to watch is {random_anime}. Enjoy Watching')

