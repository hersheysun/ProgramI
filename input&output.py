output_file=open("output.txt","w")
output_file.write("line1...\n")
output_file.write("line2..\n")

output_file.close()

output_file2=open("output2.txt","w")
print("statement1",file=output_file2)
print("statement2",file=output_file2)
output_file2.close()

input_file=open("output.txt","r")

for line in input_file:
    data=line.split(",")
    for each in data:
        print(each)
input_file.close()