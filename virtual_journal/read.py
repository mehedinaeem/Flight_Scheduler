import os

# Get the folder path from the user
folder_path = "D:\\Flight_Scheduler\\virtual_journal\\store_file"

# Check if the folder exists
if not os.path.exists(folder_path):
    print("Error: Folder does not exist.")
    exit()

# Get the file name from the user
file_name = input("Enter the name of the file to read: ")

# Check if the file exists in the folder
file_path = os.path.join(folder_path, file_name)
if not os.path.isfile(file_path):
    print("Error: File does not exist.")
    exit()

# Open the file and read its contents
with open(file_path, "r") as f:
    contents = f.read()

# Print the file contents
print(contents)
