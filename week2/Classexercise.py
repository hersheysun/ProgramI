greet="how are you?"
name="john"
day="monday"
new_str="{0} {1}. good{2}{1}!".format(greet, name, day)
print(new_str)

short_str="this"
print("{:20s} is cp1404.".format(short_str))    #left
print("{:>20} is cp1404.".format(short_str))  #align to right
print("{:^20}is cp1404.".format(short_str))     #align centre

number1= 523
print("${}".format(number1))
print("${:.2f}".format(number1))
print("${:>10s}".format(number1))