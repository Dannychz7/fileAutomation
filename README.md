File Organizer Script

Overview:
This script is designed to organize files in a specified directory into categorized subdirectories based on their file extensions. It can also detect certain keywords (e.g., "CV") in file names and group them into specific folders. The script helps maintain an orderly file system by grouping files into meaningful categories.

Features:
- Categorizes files into subdirectories such as DOCUMENTS, AUDIOS, VIDEOS, IMAGES, etc.
- Supports custom handling for files containing specific keywords in their names (e.g., files with "CV" go to Summer 2025 Internship Files).
- Skips files that are already in the correct subdirectory.
- Ensures subdirectories are only created when necessary.
- Prevents overwriting files with the same name.

How To Use:
1. Save the script to a file, e.g., organize_files.py.
2. Open a terminal or command prompt.
3. Run the script using the following command
    - python(3) "Automate Files".py <path>
    - Example: python3 autoMate.py /Users/Yourname/Downloads

Customization:
- To add new categories or file extensions, modify the SUBDIRECTORIES dictionary in the script
- Add more Logic in the pickDirectory() to make custom dirctories