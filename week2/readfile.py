file=open('number.txt','w')
file.write("17\n"  "42")
file.close()

outFile=open("number.txt","w")
number1=17
number2=42
print(number1,file=outFile)
print(number2,file=outFile)
outFile.close()
in_file=open("number.txt","r")
number1=int(in_file.readline())
number2=int(in_file.readline())
print("total:",number1+number2)
in_file.close()