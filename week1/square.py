s=input("type:")
r=s.split(' ')
for i in range(int(r[0]),int(r[1])+1):
    print(i ** 2, end=' ')
