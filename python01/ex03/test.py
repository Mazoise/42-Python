from generator import generator
import sys

print("text = \"Le Lorem Ipsum est simplement du faux texte.\"")
text = "Le Lorem Ipsum est simplement du faux texte."
print("\nTEST 1 : generator(text)")
for word in generator(text):
    print(word)
print("\nTEST 2 : generator(text, sep=\"du\")")
for word in generator(text, sep="du"):
    print(word)
print("\nTEST 3 : generator(text, option=\"shuffle\")")
for word in generator(text, option="shuffle"):
    print(word)
print("\nTEST 4 : generator(text, option=\"ordered\")")
for word in generator(text, option="ordered"):
    print(word)
print("\ntext = \"Lorem Ipsum Lorem Ipsum\"")
text = "Lorem Ipsum Lorem Ipsum"
print("\nTEST 5 : generator(text, option=\"unique\")")
for word in generator(text, option="unique"):
    print(word)
print("\nTEST 6 : generator(text, option=\"bada\") (ERROR)")
for word in generator(text, option="bada"):
    print(word)
print("\ntext = 1.0")
text = 1.0
print("\nTEST 7 : generator(text, sep=\".\") (ERROR)")
for word in generator(text, sep="."):
    print(word)
