import datetime
from recipe import Recipe


class Book:

    def __init__(self, name):
        if type(name) == str:
            self.name = name
        else:
            print("Input Error : Name should be a string")
            return
        self.recipe_list = {
            'starter': {},
            'lunch': {},
            'dessert': {},
        }
        self.last_update = datetime.datetime.today()
        self.creation_date = datetime.datetime.today()

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for rdict in self.recipe_list.values():
            for rname, rrecipe in rdict.items():
                if rname == name:
                    print(str(rrecipe))
                    return rrecipe
        print("Input Error: No such recipe\n")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        try:
            for name in self.recipe_list[recipe_type].keys():
                print(name)
        except KeyError:
            print("Input Error: Wrong type of recipe\n")

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if type(recipe) is Recipe:
            self.recipe_list[recipe.recipe_type][recipe.name] = recipe
        else:
            print("Input Error: Not a recipe\n")
            return
        self.last_update = datetime.datetime.today()
