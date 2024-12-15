# Python-Windows-Cleanup-Script
<h2>Description</h2>
<br/> 
This project demonstrates a Python script designed to clean up unnecessary and junk files on a Windows 10 system. The script automates the process of identifying and removing temporary files, logs, and other clutter that can accumulate over time, helping to free up disk space and improve system performance.
<br />
<br/> 
<br/>
<img src="https://github.com/user-attachments/assets/fc440a7f-d472-4f02-a3ec-3de0ac0e7a84"/>
<br/>  <br/>

### **Prerequisites**  

| **Service**           | **Purpose**                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **Windows 10 VM**      | Provides the testing environment for script development and execution.      |
| **Python 3.9+**        | Required to run the cleanup script.                                         |
| **os & shutil Modules**| Used for file system operations like identifying and deleting files.        |
| **Custom Junk File Script** | Generates a cluttered environment to simulate real-world conditions.   |


## Step 1: Run the junk file script

<br/> 
Project workflow: 
Prerequisite Setup: A separate script will be executed to generate junk files within a Windows 10 virtual machine, simulating a cluttered environment for testing.
Script Development and Testing: The Python cleanup script will be developed and iteratively tested to ensure it identifies and removes the junk files effectively.
Documentation: Detailed steps and images will illustrate the process, from creating the junk files to running the cleanup script and verifying its success.
<br/>

<br/> In order to simulate clutter within the virtual enviroment run the script that will generate junk files that can be found under worker_scripts <br/> 

<img src="https://github.com/user-attachments/assets/6a083a4d-81b1-4b25-825d-f91760667001"/>
<img src="https://github.com/user-attachments/assets/0048ef1f-c4f0-46ab-81cc-6db9d682f6bb"/>
<br/> Open the newly created folder wihtin the Desktop to confirm <br/>
<img src="https://github.com/user-attachments/assets/4ad02464-9ea3-4fbf-bc9a-98fcab797394"/>

## Step 2: Develop and Debug the Junk File Cleanup Script

<br/> Now I will begin to write the code to cleanup <br/> 
```.py
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

        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extensions):  # Bug: Improper handling of file extensions
                    file_path = os.path.join(directory, file)  # Bug: Incorrect path joining
                    size = os.path.getsize(file_path)
                    os.remove(file_path)  # Bug: Potential permission issue
                    files_deleted += 1
                    total_size += size
                    logging.info(f"Deleted: {file_path} ({size} bytes)")

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

```
<br/> This cleanup script is designed to identify and delete junk files (like .tmp, .log, .bak, and .txt files) from a specified directory, logging the actions taken. It configures logging to track the cleanup process in a file named cleanup_log.txt, recording the date, log level, and message. The clean_junk_files function takes a directory path and a list of file extensions to look for. It walks through the directory and its subdirectories, checking each file. If a file matches one of the junk extensions, it deletes the file and logs the action, including the file's size. If an error occurs during the cleanup (e.g., permission issues), the script logs the error message. The script sets up the target directory (JunkFiles" folder on the Desktop) and the junk file extensions. It then calls the cleanup function and prints messages to indicate the start and completion of the process. <br/>
<br/> Now lets run the script <br/>
<img src="https://github.com/user-attachments/assets/41ad3aac-2844-456a-8c6c-39dfc784814e"/>
<br/> Well the script appears to have ran but the "JunkFiles" are still present on the system and also visible on the Desktop. Let me check the cleanup_log.txt to see if there is any insight as to why. <br/>
<img src="https://github.com/user-attachments/assets/d9a0d1aa-f0d5-4f0a-925b-6952dea15385"/>
<br/> The error "endswitch first arg must be str or a tuple of str, not list", is related to the line where the script checks if a file ends with one of the specified extensions. The issue happens because file.endswith(file_extensions) is being passed a list (file_extensions), but endswith() expects a string or a tuple of strings, not a list. <br/>
<br/> To resolve this, I need to change how the endswith() method is used. It should be passed a tuple of file extensions instead of a list. Here's the modified code: <br/>

```py
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

        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(tuple(file_extensions)):  # Fix: Convert list to tuple
                    file_path = os.path.join(root, file)  # Fix: Use 'root' instead of 'directory' for correct path joining
                    size = os.path.getsize(file_path)
                    os.remove(file_path)  # Potential permission issue (ignore for now)
                    files_deleted += 1
                    total_size += size
                    logging.info(f"Deleted: {file_path} ({size} bytes)")

        logging.info(f"Cleanup complete: {files_deleted} files deleted, {total_size / 1024:.2f} KB freed.")
    except Exception as e:
        logging.error(f"Error during cleanup: {str(e)}")
```
<br/> I updated the line if file.endswith(file_extensions) to if file.endswith(tuple(file_extensions)). This converts the list of extensions to a tuple, which is what endswith() expects. I also updated the line file_path = os.path.join(directory, file) to file_path = os.path.join(root, file) so the full file path is correctly generated. The root variable provides the correct path for each file found during the os.walk() traversal. <br/>
<br/>  Now I will run the updated script and test it again <br/>




https://github.com/user-attachments/assets/2ad7673d-5a83-4936-9b1a-2fc486141da7

<br/> The script failed due to handling file extensions and now a syntax error. Will troubleshoot <br/>

```py
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

```

<br/> The script has been updated to handle file extensions more reliably. The original version incorrectly checked file extensions, but the fix now uses a more robust approach with any(file.endswith(ext) for ext in file_extensions), which ensures that the script correctly identifies files with the specified extensions, such as .tmp, .log, .bak, and .txt. Additionally, the path joining method has been corrected. The original script used an incorrect method for combining directory and file names, which could lead to errors. This has been resolved by using os.path.join(root, file), ensuring proper handling of file paths. Finally, the issue with leading zero errors in decimal integer literals has been addressed. In Python 3, integers with leading zeros are not allowed unless written in a valid format, like 0o for octal numbers. This error was avoided by ensuring no invalid number literals are used in the script. <br/>
<br/> Now I will test the new version <br/>



https://github.com/user-attachments/assets/b68aa104-7bfd-4bd8-b1e3-cb46b8f0d469




<br/> Sucess! In summary I developed a Python script designed to clean up junk files from a specified directory on a Windows 10 virtual machine. The goal was to identify and delete files with extensions such as .tmp, .log, .bak, and .txt, which can accumulate over time and take up unnecessary disk space. To begin, I created a "JunkFiles" folder on the desktop and generated several junk files for testing purposes. The script was then written to walk through the directory, identify these junk files, and delete them, while logging the actions in a cleanup_log.txt file. During testing, I encountered a few issues, including improper handling of file extensions, incorrect path joining, and a syntax error related to leading zeros in decimal integer literals. After troubleshooting, I fixed the file extension handling by using a more reliable method to check for multiple extensions, corrected the path joining to ensure proper file paths, and addressed the leading zero error by ensuring valid number literals. After making these adjustments, the script ran successfully, deleting the junk files and logging the results as expected. The final version of the script now provides a clean and efficient solution for removing unnecessary files from a system, while also keeping a detailed log of the cleanup process. <br/>
