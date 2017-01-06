names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing tuples of both initials
# splits each name and adds the first letter of each part to a tuple
full_initials = [(name.split()[0][0], name.split()[1][0]) for name in full_names]
print(full_initials)


almost_numbers = [1,2 ,3,4]
print(max(almost_numbers))
print(min(almost_numbers))
print(sum(almost_numbers)/len(almost_numbers))
# TODO: use a list comprehension to create a list of integers from this list of strings
# min =min(almost_numbers)
# max =max(almost_numbers)
# def average(almost_numbers):
#    return (sum(almost_numbers))/ len(almost_numbers)
# print("min number is:",min,"max number is:",max,"avg number is:",average)(average是函数，print输入的)

numbers=[int(number)for number in almost_numbers]
print(numbers)
#print("The average of the numbers is", sum(numbers) / len(numbers))
# TODO: use a list comprehension to create a list of all of the full_names in lowercase
# 0x000000000173CD90>
print ([s.lower() for s in names])
