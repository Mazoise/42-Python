class Recipe:

    def __init__(self, name, lvl, time, ing, desc, meal):
        try:
            assert len(name) and type(name) == str, \
                "Name should be a string"
            self.name = name
            assert type(lvl) == int and lvl >= 1 and lvl <= 5, \
                "Cooking level should be an integer between 1 and 5"
            self.cooking_lvl = lvl
            assert type(time) == int and time >= 0, \
                "Cooking time should be a positive integer"
            self.cooking_time = time
            assert (len(ing) and type(ing) == list
                    and all(type(i) is str for i in ing)), \
                "Ingredients should be a list of strings"
            self.ingredients = ing
            assert desc is None or type(desc) == str, \
                "Description should be empty or a string"
            self.description = desc
            assert (len(meal) and type(meal) == str
                    and (meal == "starter" or meal == "lunch"
                         or meal == "dessert")), \
                "Meal should be a string and be either 'starter',\
 'lunch' or 'dessert'"
            self.recipe_type = meal
        except AssertionError as e:
            print("Input Error: ", e)
            raise e

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
