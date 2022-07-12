import requests
import os
import time

Authors = ('''
############ Credits ############
#           Panguin6010         #
#           Llamalectric        #
#           nxtve               #
#           Nosson-p            #
#################################
''')
print(Authors)
time.sleep(2)
url = "https://icanhazdadjoke.com/"# Api url
user_input = input("Do you want to hear a joke? (y/n)\n")
# Get random joke from API.
def get_joke():
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    print(response.json()["joke"])
# Loop to ask user if they want a random joke.
while True:
    if user_input == "y":
        os.system('cls' if os.name == 'nt' else 'clear')# clear screen
        get_joke()
        user_input = input("Do you want to hear another joke? (y/n)\n")
    elif user_input == "n":
        print("Come back when you want to hear a joke!")
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')# clear screen
        print("I don't understand that answer please try again")
        user_input = input("Do you want to hear a joke? (y/n)\n")
        continue