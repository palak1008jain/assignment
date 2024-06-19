num1 = int(input("enter first no"))
num2 = int(input("enter second no"))
opera= input("enter operator")
if opera=="+":
    print(num1+num2)
elif opera=="-":
    print(num1-num2)
elif opera=="*":
    print(num1*num2)
elif opera=="/":
    print(num1/num2)
else:
    print("invalid input")