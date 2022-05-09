from game import GotCharacter, Stark

print("TEST 1 : arya = Stark(\"Arya\")")
arya = Stark("Arya")
print("TEST 2 : arya.__dict__")
print(arya.__dict__)
print("TEST 3 : arya.__doc__")
print(arya.__doc__)
print("TEST 4 : arya.print_house_words()")
arya.print_house_words()
print("TEST 5 : Arya is alive : ", arya.is_alive)
print("TEST 6 : arya.die()")
arya.die()
print("Arya is alive : ", arya.is_alive)
