cookbook = {
    'sandwich': {
        'name': 'sandwich',
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
        },
    'cake': {
        'name': 'cake',
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60,
        },
    'salad': {
        'name': 'salad',
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
    },
}


def print_recipe(name):
    try:
        print("Ingredients list:", cookbook[name]['ingredients'])
    except KeyError:
        print("This recipe does not exist.\n")
        return
    print("To be eaten for", cookbook[name]['meal'] + ".")
    print("Takes", cookbook[name]["prep_time"], "minutes of cooking.\n")


def del_recipe(name):
    try:
        del cookbook[name]
        print("The recipe %s was deleted.\n" % name)
    except KeyError:
        print("This recipe does not exist.\n")
        return


def print_names():
    print("")
    i = 0
    for keys in cookbook.keys():
        print(keys)
        i += 1
    if i == 0:
        print("No recipe.")
    print("")


def add_recipe(name, ing, meal, prep_t):
    cookbook[name] = {
        "ingredients": ing,
        "meal": meal,
        "prep_time": prep_t,
        "name": name
    }


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


while True:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    option = input_num()
    while option == 0:
        option = input_num()
    if option == 1:
        print("\nName of recipe :")
        name = input(">> ")
        print("\nIngredient list :(separate each ingredient with a space)")
        ing = input(">> ").split()
        print("\nMeal : ")
        meal = input(">> ")
        print("\nPreparation time :")
        try:
            time = int(input(">> "))
            add_recipe(name, ing, meal, time)
        except ValueError:
            print("Should be a number.")
    elif option == 2:
        print("\nName of recipe :")
        del_recipe(input(">> "))
    elif option == 3:
        print("\nName of recipe :")
        print_recipe(input(">> "))
    elif option == 4:
        print_names()
    elif option == 5:
        print("\nCookbook closed.")
        exit()
    else:
        print("\nThis option does not exist, \
please type the corresponding number.")
        print("To exit, enter 5.")
        option = input_num
