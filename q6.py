# Open the file in read mode
file_path = "C:/Users/Palak Jain/Downloads/example.txt"

try:
    with open(file_path, 'r') as file:
        # Read the content of the file
        file_content = file.read()

        # Print the content
        print("File Content:\n", file_content)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
