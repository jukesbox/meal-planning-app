import sqlite3
import requests
import random

"""
In this application, the user should be able to have a weekly meal plan made, based on which items they have..

"""
all_ingredients = {}
all_recipes = []
# conn = sqlite3.connect("fooddata.db")

# create tables

# for each user:
# dislikes


# what ingredients do you have?
# [user enters all ingredients]


# enter all ingredients, and their useby


def generate_package_sizes():
    # create a list of foods and their package sizes, completely dummy data for now!
    foods = "abcdefghijklmnopqrstuvwxyz"
    with open("meal-planning-app/ingredients.txt", "w") as f:
        for food in foods:
            once_opened = random.randint(1,21) # the number of days the food has once opened
            portions = random.randint(1,10) # the number of portions in each bag of food
            line = food + "," + str(portions) + "," + str(once_opened) + "\n" # make the line for the file
            f.write(line)
            print("written")


def generate_combinations():
    foods = "abcdefghijklmnopqrstuvwxyz"
    weigh = []
    # define randomised weights for the frequency of each ingredient appearing
    for i in range(26):
        weigh.append(random.randint(1,10))
    with open("meal-planning-app/recipes.txt", "w") as y:
        for x in range(20):
            num_items = random.randint(3,10)
            line = ""
            ingredients = random.choices(foods, weights=weigh, k=num_items)
            for ingredient in ingredients:
                line += ingredient + ","
            line = line[:-1] # strip the last comma
            line += "\n"
            y.write(line)

# determine if the stock can be used in exactly x meals
# determine if the stock can be used in less than x meals
# determine the minimum number of meals in which the stock can be emptied

# if any ingredient has portions > meals - discard that ingredient, and all recipes with that ingredient
# from remaining recipes, try and 'balance' ingredients
# allow (meals - portions) recipes without the ingredient
# if portions * (x+1) > meals and portions * x <= meals,,,, allow a multiple of packages of that ingredient
# 

def load_ingredients():
    with open("meal-planning-app/ingredients.txt", "r") as f:
        ingredients = f.readlines()
        for ingredient in ingredients:
            sections = ingredient.split(",")
            all_ingredients[sections[0]] = sections[1:]

def load_recipes():
    with open("meal-planning-app/recipes.txt", "r") as f:
        recipes = f.readlines()
        for recipe in recipes:
            this_recipe = recipe.split(",")
            all_recipes.append(this_recipe)

def discard_ingredients(num_meals):
    available_ings = []
    for ing in all_ingredients:
        # add the available ingredients to the list
        if all_ingredients[ing][0] <= num_meals:
            available_ings.append(ing)
    return available_ings

def discard_recipes(ings):
    available_recipes = []
    for recipe in all_recipes:
        # discard the recipe if it contains something not in the available ings
        for item in recipe:
            if item not in ings:
                useable = False
        if useable:
            available_recipes.append(recipe)
    return available_recipes

def choose_recipes():
    available_recipes = discard_recipes(discard_ingredients(7))
    pass


# what is the smallest number of ingredients that can be bought to make a meal?



"""
foods(FoodID, FoodName, ShelfLife)
user_foods(UserID, FoodID, UseBy, amount, unit)
user(UserID, UserName)
user_dislikes(UserID, FoodID)
"""





def add_ingredients_that_exist():
    # if the table of ingredients doesn't exist make it!
    pass


def make_meal_plan():
    # how many people on each day
    # how many days - can be left blank - will make as many as possible....

    # what ingredients you already have
    pass


# pantry
# fridge
# freezer

def fridge():
    # enter the contents of your fridge here
    pass

def freezer():
    # enter the contents of your freezer here
    pass

def cupboard():
    # enter non-perishable items here
    # these are items that can last quite a while and do not need to be used up at the end of the week
    pass

def ran_out():
    # enter ingredients currently in the cupboard that you've ran out of....
    pass


def add_a_recipe():
    #prompts the user to add in the ingredients and amounts of their own recipe(s)
    pass

def cupboard_check():
    pass


if __name__ =="__main__":
    print("hello there")
    # generate_package_sizes()
    # generate_combinations()