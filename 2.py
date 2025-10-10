#Generate a random 2-line funny story by mixing random characters, places, and actions.

#how_many = int(input("How many stories do you want? "))

import random 
characters = ["a sleepy panda", "an alien", "a pirate", "a robot"] 
places = ["in the jungle", "on Mars", "at a tech fest", "in the library"] 
objects = ["a laptop", "a treasure map", "a sandwich", "a phone"] 
actions = ["started coding", "fell asleep", "built a rocket", "lost their WiFi"] 

i=1
how_many = int(input("How many stories do you want? :"))
while i <= how_many:
    character = random.choice(characters)
    place = random.choice(places)
    object = random.choice(objects)
    action = random.choice(actions)
    print(i,".","Once upon a time",character,"found",object,place,"and",action )
    i += 1




# TODO: use random.choice() to pick one from each list 
# TODO: print something like: 
# "Once upon a time, ___ found ___ ___ and ___!"