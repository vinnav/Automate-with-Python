import os, sys

# Create a Mad Libs program that reads in text files and lets the user add
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB 
# appears in the text file.

text = open(str(sys.argv[1]), "r")
textContent = text.read()
text.close()

adjective = input("Insert adjective: ")
noun = input("Insert noun: ")
verb = input("Insert verb: ")

textContent = textContent.replace("ADJECTIVE", adjective)
textContent = textContent.replace("NOUN", noun)
textContent = textContent.replace("VERB", verb)


# The ADJECTIVE panda walked to the NOUN and then VERB
text = open(str(sys.argv[1]), "w")
text.write(textContent)