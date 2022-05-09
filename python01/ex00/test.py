from book import Book
from recipe import Recipe
import string


def input_num():
    option = input(">> ")
    try:
        int(option)
    except ValueError:
        print("\nThis option does not exist,\
 please type the corresponding number.")
        print("To exit, enter 5.")
        return 0
    return int(option)


print("Test 1 : Creating recipe book!")
book = Book("My Cooking Book")
print("\n" + book.name, "- Creation:", book.creation_date, "- Last update:",
      book.last_update, "\n")
print("Test 2 : Getting starters (empty)")
book.get_recipes_by_types("starter")
print("Test 3 : Adding recipe Tourte in starters")
tourte = Recipe("Tourte", 3, 40,
                ["pate", "creme", "oeufs", "viande", "legumes"],
                "Cuire", "starter")
book.add_recipe(tourte)
print("Test 4 : Adding recipe Tourte even if it already exists")
book.add_recipe(tourte)
book.get_recipes_by_types("starter")
print("Test 5 : Getting Tourte recipe")
book.get_recipe_by_name("Tourte")
print("Test 6 : Adding string as recipe (wrong input)")
book.add_recipe("wrong input")
print("Test 7 : Getting recipe that doesn't exist")
book.get_recipe_by_name("Gateau")
print("Test 8 : Adding Gateau recipe")
gateau = Recipe("Gateau", 2, 30,
                ["chocolat", "oeufs", "farine", "beurre"],
                "Melanger, cuire", "dessert")
book.add_recipe(gateau)
book.get_recipe_by_name("Gateau")
print("Test 9 : Getting all recipes")
print("Starters:")
book.get_recipes_by_types("starter")
print("Lunchs:")
book.get_recipes_by_types("lunch")
print("Desserts:")
book.get_recipes_by_types("dessert")
print("Test 10 : Asking for wrong recipe type")
book.get_recipes_by_types("cocktail")
print("Test 11 : Adding recipe in starters")
quiche = Recipe("Quiche", 2, 45,
                ["pate", "creme", "oeufs", "lardons", "fromage"],
                "", "starter")
book.add_recipe(quiche)
book.get_recipe_by_name("Quiche")
print("Creation time:", book.creation_date,
      "Last update:", book.last_update, "\n")
print("Test 12 : Getting all starters")
book.get_recipes_by_types("starter")
try:
    print("Test 13 : Adding empty name recipe")
    empty_name = Recipe("", 2, 45,
                        ["pate", "creme", "oeufs", "lardons", "fromage"],
                        "Cuire au four", "starter")
    book.add_recipe(empty_name)
except AssertionError:
    print("Test 13 : Error catched")
try:
    print("Test 14 : Adding wrong ingredients recipe")
    empty_ing = Recipe("Quiche", 2, 45, ["bada", 1.2],
                       "Cuire au four", "starter")
    book.add_recipe(empty_ing)
except AssertionError:
    print("Test 14 : Error catched")
try:
    print("Test 15 : Adding wrong type recipe")
    empty_type = Recipe("Quiche", 2, 45,
                        ["pate", "creme", "oeufs", "lardons", "fromage"],
                        "Cuire au four", "cocktail")
    book.add_recipe(empty_type)
except AssertionError:
    print("Test 15 : Error catched")
try:
    print("Test 16 : Adding not integer time recipe")
    empty_time = Recipe("Quiche", 2, "bada",
                        ["pate", "creme", "oeufs", "lardons", "fromage"],
                        "Cuire au four", "starter")
    book.add_recipe(empty_time)
except AssertionError:
    print("Test 16 : Error catched")
