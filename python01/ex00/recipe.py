class Recipe:

    def __init__(self, name, lvl, time, ing, desc, meal):
        if type(name) == str:
            self.name = name
        else:
            print("Input Error: Name should be a string\n")
            return
        if type(lvl) == int and lvl >=1 and lvl <= 5:
            self.cooking_lvl = lvl
        else:
            print("Input Error: Cooking level should be a number between 1 and 5\n")
            return
        if type(time) == int and time >= 0:
            self.cooking_time = time
        else:
            print("Input Error: Time should be a positive number\n")
            return
        if type(ing) == list and all(type(i) is str for i in ing):
            self.ingredients = ing
        else:
            print("Input Error: Ingredients should be in a list\n")
            return
        if desc is None or type(desc) == str:
            self.description = desc
        else:
            print("Input Error: If you want to add a description it should be a string\n")
            return
        if type(meal) == str and (meal == "starter" or meal == "lunch" or meal == "dessert"):
            self.recipe_type = meal
        else:
            print("Input Error: Recipe type should be either \"meal\", \"lunch\" or \"dessert\"\n")
            return

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "\nRecipe : " + self.name
        txt += "\nRecipe type : " + self.recipe_type
        txt += "\nCooking level : " + str(self.cooking_lvl)
        txt += " / 5\nCooking time : " + str(self.cooking_time)
        txt += " min\nIngredients : " + str(self.ingredients)
        txt += "\nDescription: " + self.description + "\n"
        return txt