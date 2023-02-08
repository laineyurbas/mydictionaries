# 1) print out the value for the key 'history' using the dictionary below

## this dict only has one "key" clas, the rest are keys of dictranaries
sampleDict = {
    "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
}
# 1_____

score = sampleDict["class"]["student"]["marks"]["history"]
print(score)
# or do this: print(sampleDict["class"]["student"]["marks"]["history"])


# 2) Add 2 inches to the son's height.
## YOU CANT HARD CODE BC IT SAYS ADD NOT SET $$$$
dict = {
    "son's name": "Lucas",
    "son's eyes": "green",
    "son's height": 32,
    "son's weight": 25,
}

dict["son's height"] += 2
print(dict)

# 3) Given a Python dictionary, Change Brad’s salary to 8500
#### change means u should hard code

sampleDict = {
    "emp1": {"name": "Jhon", "salary": 7500},
    "emp2": {"name": "Emma", "salary": 8000},
    "emp3": {"name": "Brad", "salary": 6500},
}


# 3___
sampleDict["emp3"]["salary"] = 8500
print(sampleDict)

# 4 )Given the dictionary below, add a new key - 'work' with the values shown below:
#       "work": ["Apology", "Phaedo", "Republic", "Symposium"]

dict = {
    "name": "Plato",
    "country": "Ancient Greece",
    "born": -427,
    "teacher": "Socrates",
    "student": "Aristotle",
}
###4
dict["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]
print(dict)
