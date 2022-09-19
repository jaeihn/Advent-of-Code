# 2015 - DAY 15 - SCIENCE FOR HUNGRY PEOPLE
# https://adventofcode.com/2015/day/15


import os
import regex

from itertools import combinations_with_replacement
from math import prod
from collections import Counter


with open(os.path.dirname(__file__)+'/inputs/day15.txt', 'r') as f:
    instructions = f.read().split('\n')[:-1]
f.close()



# Part 1 

class Ingredient:
    def __init__(self, instruction):

        ingredient_info = instruction.split(':')
        properties = [int(d) for d in regex.findall(r'-?\d', ingredient_info[1])]

        self.name = ingredient_info[0].lower()        
        self.capacity = properties[0]
        self.durability = properties[1]
        self.flavor = properties[2]
        self.texture = properties[3]
        self.calories = properties[4]
    
    def print_info(self):
        print(self.name, self.capacity, self.durability, self.flavor, self.texture, self.calories)


ingredients = {}

for i in instructions:
    ingredient = Ingredient(i)
    ingredients[ingredient.name] = ingredient



def total_score(recipe):

    score = {
        'capacity' : 0,
        'durability' : 0,
        'flavor' : 0,
        'texture' : 0,
        'calories' : 0
    }

    for ingredient, tsp in recipe.items():
        score['capacity'] += tsp * ingredients[ingredient].capacity
        score['durability'] += tsp * ingredients[ingredient].durability
        score['flavor'] += tsp * ingredients[ingredient].flavor
        score['texture'] += tsp * ingredients[ingredient].texture
        score['calories'] = 1

    for criteria, pts in score.items():
        if pts < 0: 
            score[criteria] = 0

    return prod(score.values())


recipes = list(combinations_with_replacement(ingredients.keys(),100))

scored_recipes = []
for r in recipes:
    parsed_recipe = dict(Counter(r))
    scored_recipes.append((parsed_recipe, total_score(parsed_recipe)))


print(max(scored_recipes, key=lambda x:x[1]))


# Part 2 



def total_score(recipe):

    score = {
        'capacity' : 0,
        'durability' : 0,
        'flavor' : 0,
        'texture' : 0,
        'calories' : 0
    }

    for ingredient, tsp in recipe.items():
        score['capacity'] += tsp * ingredients[ingredient].capacity
        score['durability'] += tsp * ingredients[ingredient].durability
        score['flavor'] += tsp * ingredients[ingredient].flavor
        score['texture'] += tsp * ingredients[ingredient].texture
        score['calories'] += tsp * ingredients[ingredient].calories

    for criteria, pts in score.items():
        if pts < 0: 
            score[criteria] = 0

    if score['calories'] != 500:
        return 0 
    else: 
        return score['capacity']*score['durability']*score['flavor']*score['texture']


recipes = [dict(Counter(r)) for r in list(combinations_with_replacement(ingredients.keys(),100))]

scored_recipes = []
for r in recipes:
    scored_recipes.append((r, total_score(r)))

print(max(scored_recipes, key=lambda x:x[1]))

