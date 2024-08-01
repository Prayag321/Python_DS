# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title : Python script that takes input from the user and displays that input back in
# upper and lower cases


def to_upper_case(s):
    """
    Converts a given string to upper case without using inbuilt upper() function.

    Parameters:
    s (str): The input string.

    Returns:
    result(str): The input string converted to upper case.
    """
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            # Convert to upper case by subtracting 32 from ASCII value
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def to_lower_case(s):
    """
    Converts a given string to lower case without using inbuilt lower() function.

    Parameters:
    s (str): The input string.

    Returns:
    str: The input string converted to lower case.
    """
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            # Convert to lower case by adding 32 to ASCII value
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def main():
    user_input = input("Please enter a string: ")
    upper_case = to_upper_case(user_input)
    lower_case = to_lower_case(user_input)
    print(f"Upper case: {upper_case}")
    print(f"Lower case: {lower_case}")

if __name__ == "__main__":
    main()
