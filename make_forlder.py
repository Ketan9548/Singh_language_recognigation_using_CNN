import os

# Define the base directory where you want to create the folders
base_directory = "/path/to/your/directory"

# Check if the base directory exists, if not, create it
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

# Loop through ASCII values for uppercase letters (65 to 90)
for ascii_value in range(65, 91):
    folder_name = chr(ascii_value)  # Convert ASCII value to character
    folder_path = os.path.join(base_directory, folder_name)

    # Check if folder already exists, if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")