username= str(input("what is your name"))
vowel="aeiouAEIOU"
count=0
for each in username:
    if each in username:
        count +=1
print("out of {}letter,{}has {} vowels".format(len(username),username,count))