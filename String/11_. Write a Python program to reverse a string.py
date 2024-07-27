# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title :Write a Python program to reverse a string
def reverse_string(s):
    """
    Reverses the given string.

    Parameters:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return s[::-1]

def main():
    user_input = input("Please enter a string to reverse: ")
    reversed_string = reverse_string(user_input)
    print("Reversed string:", reversed_string)

if __name__ == "__main__":
    main()
