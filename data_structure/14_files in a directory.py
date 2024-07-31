# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 
# @Title:  Write a Python program to list all files in a directory in Python

import os
def list_files_in_directory(directory_path):
    """
    List all files in the given directory.

    Parameters:
    directory_path (str): Path to the directory

    Returns:
    list: List of file names in the directory
    """

    return os.listdir(directory_path)
def main():
  directory_path = "E:\Development\Pratice\Python_DS"
  files = list_files_in_directory(directory_path)
  for file in files:
    print(file)
if __name__ == "__main__":
    main()