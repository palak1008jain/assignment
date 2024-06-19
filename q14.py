
lines = []


while True:

    l = input()

    # Check if the entered line is not empty (non-empty string)
    if l:
        # Convert the entered line to uppercase and append it to the 'lines' list
        lines.append(l)
    else:
        # If the entered line is empty, break out of the loop
        break;

# Iterate through each line in the 'lines' list
for l in lines:
    # Print each line (converted to uppercase) from the 'lines' list
    print(l)
