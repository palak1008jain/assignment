nterms=int(input("enter the n number"))
n1=0
n2=1
count=0

if nterms<1:
    print("undefined")
elif nterms==1:
    print("n1")
else:
    while count< nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
    
