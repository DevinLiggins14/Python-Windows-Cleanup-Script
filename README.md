# Python-Windows-Cleanup-Script
<h2>Description</h2>
<br/> 
This project demonstrates a Python script designed to clean up unnecessary and junk files on a Windows 10 system. The script automates the process of identifying and removing temporary files, logs, and other clutter that can accumulate over time, helping to free up disk space and improve system performance.
<br />
<br/> 
<br/>
<img src=""/>
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
<img src=""/>
<br/> <br/>
<img src=""/>
<img src=""/>
<img src=""/>
<img src=""/>
<br/> <br/>
<img src=""/>
<img src=""/>
<img src=""/>
<img src=""/>
<br/> <br/>
<img src=""/>
<img src=""/>
<img src=""/>
<img src=""/>
<br/> <br/>
<img src=""/>
<img src=""/>
<img src=""/>
<img src=""/>
<br/> <br/>
<img src=""/>
<img src=""/>
<img src=""/>
<img src=""/>
<br/> <br/>
<img src=""/>
<img src=""/>
<img src=""/>
<img src=""/>
<br/> <br/>
<img src=""/>
<img src=""/>
<img src=""/>
<img src=""/>
<br/> <br/>
<img src=""/>
<img src=""/>
<img src=""/>
<img src=""/>
<br/> <br/>



