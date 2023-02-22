noun = input("Noun: ")
verb = input("Verb: ")
noun2 = input("Noun (plural): ")
noun3 = input("Noun (plural): ")
verb2 = input("Verb: ")
noun4 = input("Noun: ")

# print(example) 
# print(noun) 

madlibs = "Hey! Welcome to my " + noun + ". Here, we " + verb + " about " + noun2 + " and we have fun with " + noun3 + ". Make sure you " + verb2 + " to my " + noun4 + "."
madlibs = f"Hey! Welcome to my {noun}. Here, we {verb} about {noun2} and we have fun with {noun3}. Make sure you {verb2} to my {noun4}."

print(madlibs)