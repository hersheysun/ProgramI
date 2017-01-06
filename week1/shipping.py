shippingCost=float(input("Enter cost: "))
shippingnumber=int(input("Enter number of items:"))
totalfee=(shippingCost*shippingnumber)
while(shippingnumber>=0):
    if shippingCost>100:
        shippingCost= shippingCost-shippingCost*0.1
        print("the totalfee are:",totalfee)
    elif shippingCost<100and shippingCost>0:
        print("the totalfee are",totalfee)
    else:
        print("you type in number can small than 0")
    break
    shippingCost=float(input("Enter cost: "))
    shippingnumber=int(input("Enter number of items:"))
print("done")