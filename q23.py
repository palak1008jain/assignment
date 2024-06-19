f_or_c= input("enter f for fahreheit to celsius and c for celsius to fahrenheit")
temp = float(input("enter temp"))
if f_or_c == "f":
    celsius=(temp- 32)/1.8
    print("temp in c is",celsius)
else:
    fahren = (temp* 1.8)+32
    print("temp in fahren is",fahren)

