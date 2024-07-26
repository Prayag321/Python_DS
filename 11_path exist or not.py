# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title:Python program to check whether a file exists

import os

def file_exists(file_path):
    """
    Check if a file exists at the given file path.

    Parameters:
    file_path (str): Path to the file to check

    Returns:
    bool: True if the file exists, False otherwise
    """
    return os.path.isfile(file_path)

def main():
    file_path = input("Enter the path of the file to check: ")
    if file_exists(file_path):
        print("The file exists.")
    else:
        print("The file does not exist.")

if __name__ == "__main__":
    main()
