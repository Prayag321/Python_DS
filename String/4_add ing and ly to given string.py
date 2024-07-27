# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title : Python program to modify a string based on its length and suffix

def modify_string(input_string):
    """
    Description:
        This function modifies a string based on its length and suffix.
        - If the string length is less than 3, it returns the string unchanged.
        - If the string length is at least 3 and does not end with 'ing', it appends 'ing' to the string.
        - If the string length is at least 3 and ends with 'ing', it appends 'ly' instead.
    Parameters:
        input_string (str): The string to be modified.
    Returns:
        str: The modified string.
    """
    if len(input_string) < 3:
        return input_string
    if input_string.endswith('ing'):
        return input_string + 'ly'
    return input_string + 'ing'

def main():
    
    user_string = input("Enter a string: ")
    modified_string = modify_string(user_string)
    print(f"The modified string is: {modified_string}")

if __name__ == "__main__":
    main()
