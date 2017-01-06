name=["alice","tom","join"]
ages=[10,40,25]
print(name[1])
print(name[-1])

while True:
    name=input("enter a name:")

    if name=="":
      break
    name.append(name)
print(name+name)

