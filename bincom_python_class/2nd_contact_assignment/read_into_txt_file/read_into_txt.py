file = open("my_name.txt", "w")
file.write("Olamilekan Emmanuel Oladipupo")
file.close()
with open("my_name.txt", "r") as file:
    for words in file:
        for word in words.split():
            print(word)

import os
print("Here is my current working directory ", os.getcwd())





