import os
import shutil

# Get the directory that needs to be organized
folder_path = input("Enter the folder path: ").strip().strip('"')

# Validate the folder path
if not os.path.isdir(folder_path):
    print("Error: The folder path does not exist or is not a directory.")
    exit()


# File categories mapped to their supported extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar"]
}


def organize_files(folder_path):
    """
    Organizes files into categorized folders based on their extensions.
    """

    # Iterate through every item inside the selected directory
    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        # Skip directories and process only files
        if not os.path.isfile(file_path):
            continue

        # Extract the file extension and convert it to lowercase
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Track whether the file was categorized
        matched = False

        # Check which category the file belongs to
        for folder_name, extensions in file_types.items():

            if extension in extensions:

                # Create the destination folder if it doesn't exist
                target_folder = os.path.join(folder_path, folder_name)
                os.makedirs(target_folder, exist_ok=True)

                # Move the file to its corresponding folder
                shutil.move(file_path, os.path.join(target_folder, filename))

                print(f"Moved: {filename} → {folder_name}")

                matched = True

                # Stop checking once the file has been categorized
                break

        # Inform the user about unsupported files
        if not matched:
            print(f"Skipped: {filename} (unsupported file type)")


if __name__ == "__main__":
    organize_files(folder_path)
