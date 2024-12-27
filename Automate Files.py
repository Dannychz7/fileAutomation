import os
import sys
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIOS": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png'],
    "Pictures": ['.HEIC'],
    "Trash": ['.dmg', '.zip', '.csv', '.iso', '.php']
}

def pickDirectory(file_extension, file_name):
    file_name_lower = file_name.lower()
    if "cv" in file_name_lower:
        return "Summer 2025 Internship Files"

    for category, suffixes in SUBDIRECTORIES.items():
        if file_extension in suffixes:
            return category
    return "MISC"

def organizeDirectory(directory_path):
    for item in os.scandir(directory_path):
        if item.is_dir():
            continue  # Skip directories

        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType, filePath.name)

        directoryPath = Path(directory_path).joinpath(directory)

        # Check if the file is already in the correct directory
        if filePath.parent == directoryPath:
            print(f"Skipping {filePath.name}, already in {directoryPath}")
            continue

        # Create the directory if it doesn't exist
        if not directoryPath.exists():
            directoryPath.mkdir()
            print(f"Created directory: {directoryPath}")

        # Move the file to the target directory
        newFilePath = directoryPath.joinpath(filePath.name)
        if newFilePath.exists():
            print(f"Skipping {filePath.name}, already exists in {directoryPath}")
            continue

        filePath.rename(newFilePath)
        print(f"Moved {filePath.name} to {directoryPath}")

if __name__ == "__main__":
    # Check if the path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <path>")
        sys.exit(1)

    target_path = Path(sys.argv[1])

    # Check if the provided path exists
    if not target_path.is_dir():
        print(f"Error: The path '{target_path}' does not exist or is not a directory.")
        sys.exit(1)

    organizeDirectory(target_path)

