# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 
# @Title: Python program to call an external command

import subprocess

def call_external_command(command):
    """
    Call an external command and return its output.

    Parameters:
    command (str): The command to execute

    Returns:
    str: The standard output from the command
    """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def main():
    command = "dir"
    output = call_external_command(command)
    print("Command Output:")
    print(output)

if __name__ == "__main__":
    main()
