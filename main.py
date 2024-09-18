import sqlite3
import requests

"""
In this application, the user should be able to have a weekly meal plan made, based on which items they have..

"""

conn = sqlite3.connect("fooddata.db")

# create tables

# for each user:
# dislikes


# what ingredients do you have?
# [user enters all ingredients]


# enter all ingredients, and their useby


"""
foods(FoodID, FoodName, ShelfLife)
user_foods(UserID, FoodID, UseBy, amount, unit)
user(UserID, UserName)
user_dislikes(UserID, FoodID)
"""
def add_ingredients_that_exist():
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


def add_a_recipe():
    #prompts the user to add in the ingredients and amounts of their own recipe(s)
    pass

def cupboard_check():
    pass