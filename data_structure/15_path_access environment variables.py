# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title: Write a python program to access environment variables

import os

def get_environment_variable(var_name):
    """
    Get the value of the specified environment variable.

    Parameters:
    var_name (str): Name of the environment variable

    Returns:
    str: Value of the environment variable, or None if it does not exist
    """
    return os.environ.get(var_name) #can use os.getenv(var)

def main():

    var_name = input("Enter the name of the environment variable to access: ")
    var_value = get_environment_variable(var_name)
    
    if var_value is not None:
        print(f"The value of the environment variable '{var_name}' is: {var_value}")
    else:
        print(f"The environment variable '{var_name}' does not exist.")

if __name__ == "__main__":
    main()
