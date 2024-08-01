'''
    @Author: Prayag Bhoir
    @Date: 01-08-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 01-08-2024 
    @Title : Python program to get the last part of a string before a specified character
'''

def get_last_part_before_char(text, char):
    """
    Description:
        This function extracts the last part of the string before the specified character.
    Parameters:
        text : string from which to extract the part
        char : character before which to extract
    Return:
        string : part of the text before the specified character
    """

    position = text.rfind(char)
    
    if position == -1:
        return text
    
    return text[:position]

def main():

    text = "prayag bhoir"
    char = 'b'

    result = get_last_part_before_char(text, char)
    
    print(f"The part of the string before '{char}' is: '{result}'")

if __name__ == "__main__":
    main()
