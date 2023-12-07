from pathlib import Path
import shutil

def organize_files(source_dir):
    source_path = Path(source_dir)

    # Define file type categories and their respective directory names
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"]
        # Add more categories and file extensions as needed
    }

    # Ensure the source directory exists
    if not source_path.exists():
        print("Source directory does not exist.")
        return

    # Create directories for each file type
    for category, extensions in file_types.items():
        category_dir = source_path / category
        category_dir.mkdir(exist_ok=True)

    # Move files to respective directories
    for file in source_path.iterdir():
        if file.is_file():
            file_extension = file.suffix.lower()
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    destination_dir = source_path / category / file.name
                    shutil.move(str(file), str(destination_dir))
                    break

if __name__ == "__main__":
    source_directory = input("Enter the path of the directory to organize: ")
    organize_files(source_directory)

