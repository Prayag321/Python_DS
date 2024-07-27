# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 
# @Title : Python program to count the number of characters in a string

def count_character_frequency(input_string):
    """
    Description:
        This function accepts a string and returns a dictionary with the frequency of each character in the string.
    Parameters:
        input_string (str): The string whose character frequency is to be calculated.
    Returns:
        dict: A dictionary with characters as keys and their respective frequencies as values.
    """
    frequency = {} #declare empty dict
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def main():
    user_string = input("Enter a string: ")
    character_frequency = count_character_frequency(user_string)
    print(f"The character frequency in the string is: {character_frequency}")

if __name__ == "__main__":
    main()
