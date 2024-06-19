import string

test = input("enter string")


print("The original string is : " + test)


for punctuation in string.punctuation:
    test = test.replace(punctuation, '')


print("The string after punctuation filter : " + test)