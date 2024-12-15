import os
import logging

# Configure logging
logging.basicConfig(
    filename="cleanup_log.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def clean_junk_files(directory, file_extensions):
    """
    Identify and delete junk files in the specified directory.
    
    Args:
        directory (str): Path to the directory containing junk files.
        file_extensions (list): List of file extensions to consider as junk.
    """
    try:
        files_deleted = 0
        total_size = 0

        # Walk through the directory and its subdirectories
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Check if the file has a junk extension
                if any(file.endswith(ext) for ext in file_extensions):
                    file_path = os.path.join(root, file)  # Corrected path joining
                    size = os.path.getsize(file_path)
                    os.remove(file_path)  # Remove the file
                    files_deleted += 1
                    total_size += size
                    logging.info(f"Deleted: {file_path} ({size} bytes)")

        # Log the cleanup result
        logging.info(f"Cleanup complete: {files_deleted} files deleted, {total_size / 1024:.2f} KB freed.")
    except Exception as e:
        logging.error(f"Error during cleanup: {str(e)}")

if __name__ == "__main__":
    # Configuration
    target_directory = os.path.join(os.path.expanduser("~"), "Desktop", "JunkFiles")  # Correct directory assumed
    junk_extensions = [".tmp", ".log", ".bak", ".txt"]  # Extensions to clean

    print("Starting cleanup process...")
    clean_junk_files(target_directory, junk_extensions)
    print("Cleanup process completed. Check cleanup_log.txt for details.")
