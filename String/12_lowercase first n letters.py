# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title :Write a Python program to lowercase first n characters in a string
def lowercase_first_n_characters(s, n):
    """
    Converts the first n characters of a string to lowercase.

    Parameters:
    s (str): The original string.
    n (int): The number of characters to convert to lowercase.

    Returns:
    str: The string with the first n characters converted to lowercase.
    """
    if n > len(s):
        n = len(s)
    return s[:n].lower() + s[n:]

def main():
    user_input = input("Please enter a string: ")
    n = int(input("Enter the number of characters to lowercase: "))
    result = lowercase_first_n_characters(user_input, n)
    print("Result:", result)

if __name__ == "__main__":
    main()
