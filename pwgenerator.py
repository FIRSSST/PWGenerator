import string
import random

characters = ""
uppercase = input("Uppercase? Y or N \n")
lowercase = input("Lowercase? Y or N \n")
special_characters = input("Special characters? Y or N \n")
numbers = input("Numbers? Y or N \n")


if uppercase == "Y" and lowercase == "Y":
    characters = string.ascii_letters
elif uppercase == "Y" and lowercase == "N":
    characters = string.ascii_uppercase
elif uppercase == "N" and lowercase == "Y":
    characters = string.ascii_lowercase

if special_characters == "Y":
    characters += "!@#$%^&*()"
if numbers == "Y":
    characters += string.digits

characters = list(characters)

length = int(input("Length? \n"))

random.shuffle(characters)
pw = ""
pw = pw.join(characters[0:length])
print("\n" + pw)