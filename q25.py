with open("C:/Users/Palak Jain/Downloads/example.txt", 'r') as firstfile, open("C:/Users/Palak Jain/Downloads/sample2.txt", 'a') as secondfile:
    for line in firstfile:
       
        secondfile.write(line)
