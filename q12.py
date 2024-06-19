num=int(input("enter the number"))
sum=0
while num>0:
    dig=num%10
    sum=sum+dig
    num= int(num/10)
print(sum)