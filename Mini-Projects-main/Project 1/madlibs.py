
# fill in the blanks with the required words.

# to read the paragraph
print("One of the _____ problems facing the world today is global warming. \
Many scientists believe that our production of carbon dioxide and \
other greenhouse gases is having a heating effect on the atmosphere and this \
_____ be very dangerous for human life.\
We ____ examine the problem of global warming and suggest some ways of solving it. ")


# obtain input
adj = input("Adjective : ")
gas = input("Greenhouse gas : ")
noun1 = input("Noun : ")
adverb1 = input("Adverb : ")
noun2 = input("Noun : ")
adverb2 = input("Adverb : ")
verb = input("Verb : ")


madlib = f"One of the {adj} problems facing the world today is global warming. \
Many scientists believe that our production of {gas} and \
other greenhouse gases is having a {noun1} effect on the atmosphere and this {adverb1} \
be very dangerous for human {noun2}. \
We {adverb2} examine the problem of global warming and suggest some ways of {verb} it."

# print the completely filled paragraph
print(madlib)
