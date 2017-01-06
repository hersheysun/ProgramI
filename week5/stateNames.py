
# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"a":"2", "colection": "1", "fun" :"1", "is" : "3", "it":"1", "nice":"1", "of":"2","thing":"1","this":"2","words":"2"  }
print(STATE_NAMES)

state = input("Enter short state: ")
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ")

print("{:{}}:{}".format(a,b,c))