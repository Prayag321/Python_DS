# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title : Python program to replace all occurrences of first character with '$' except the first occurrence

def replace_char(input_string):
    """
    Description:
        This function accepts a string and returns a new string where all occurrences of the first character
        have been replaced with '$', except for the first character itself.
    Parameters:
        input_string (str): The string to process.
    Returns:
        str: The processed string with replacements.
    """
    if not input_string:
        return input_string #for empty string

    first_char = input_string[0]
    replaced_string = first_char + input_string[1:].replace(first_char, '$')
    return replaced_string

def main():
    user_string = input("Enter a string: ")
    result_string = replace_char(user_string)
    print(f"The modified string is: {result_string}")

if __name__ == "__main__":
    main()
