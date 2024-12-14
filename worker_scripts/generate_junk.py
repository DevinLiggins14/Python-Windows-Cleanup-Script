import os
import random
import string

def generate_random_string(length):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_junk_files(directory, num_files, file_size_kb, file_extensions):
    """
    Create junk files with random content.

    Args:
        directory (str): Directory to create junk files in.
        num_files (int): Number of files to create.
        file_size_kb (int): Size of each file in kilobytes.
        file_extensions (list): List of file extensions to randomly choose from.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(num_files):
        file_name = f"junk_{i}_{generate_random_string(5)}{random.choice(file_extensions)}"
        file_path = os.path.join(directory, file_name)

        try:
            with open(file_path, 'wb') as f:
                f.write(os.urandom(file_size_kb * 1024))  # Write random bytes to file
            print(f"Created: {file_path}")
        except Exception as e:
            print(f"Failed to create {file_path}: {e}")

if __name__ == "__main__":
    # Configuration
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "JunkFiles")
    number_of_files = 50  # Total junk files to create
    size_per_file_kb = 10  # Size of each file in KB
    extensions = [".tmp", ".log", ".bak", ".txt"]  # Junk file extensions

    # Generate junk files
    create_junk_files(desktop_path, number_of_files, size_per_file_kb, extensions)

    print("Junk file generation completed. Check the 'JunkFiles' folder on your desktop.")
