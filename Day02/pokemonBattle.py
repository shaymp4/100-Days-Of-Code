# Day 2 – Pokémon Tuple Practice 🧢

import random

# Pokémon trainer data stored in a tuple
pokeTuple = ('Oshawott', 'Shay', 2)
(Pokemon, Trainer, Gym_Badges) = pokeTuple

#Print trainer info
def trainerProfile():
    return f"""
Trainer: {Trainer}
Pokémon: {Pokemon}
Gym Badges: {Gym_Badges}
"""

#Search for a Pokémon by name
def pokeSearch(pokemon):
    if pokemon.lower() == Pokemon.lower():
        return "Pokémon found!"
    else:
        return "Unable to locate that Pokémon."

#Simple battle simulator against a random enemy
def battle():
    enemies = ['Gengar', 'Charizard', 'Snorlax', 'Pikachu']
    enemy = random.choice(enemies)
    outcome = random.choice(['win', 'lose'])

    print(f"\nA wild {enemy} appeared!")

    if outcome == 'win':
        new_badges = Gym_Badges + 1
        print(f"{Trainer} and {Pokemon} defeated {enemy} and earned a new badge!")
        print(f"Updated Badge Count: {new_badges}")
    else:
        print(f"{Trainer} and {Pokemon} were defeated by {enemy}...")

#Test the functions
print(trainerProfile())
print(pokeSearch('Oshawott'))
print(pokeSearch('Bulbasaur'))
battle()