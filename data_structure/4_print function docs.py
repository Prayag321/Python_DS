# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title : Python program to print the documentation of a built-in function

def print_function_docs(func):
    """
    Description:
        This function prints the documentation (syntax and description) of a given built-in Python function.
    Parameters:
        func (function): The built-in Python function whose documentation is to be printed.
    Returns:
        None
    """
    return help(func)

def main():
    user_input = input("Enter the function name :")
    print(f"Documentation for the {user_input} function:")
    print_function_docs(user_input)

if __name__ == "__main__":
    main()
