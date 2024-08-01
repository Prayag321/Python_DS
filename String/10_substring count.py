'''
    @Author: Prayag Bhoir
    @Date: 01-08-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 01-08-2024 
    @Title : Python program to count occurrences of a substring in a string
'''

def count_substring_occurrences(text, substring):
    """
    Description:
        This function counts the number of occurrences of a substring in a string.
    Parameters:
        text : string in which to search
        substring : substring to search for
    Return:
        int : number of occurrences
    """
    text_length = len(text)
    substring_length = len(substring)
    count = 0

    for i in range(text_length - substring_length + 1):
        if text[i:i + substring_length] == substring:
            count += 1

    return count

def main():
    text = "This is a test string. Testing is fun. Test test test."
    substring = "test"

    occurrences = count_substring_occurrences(text.lower(), substring.lower())   
    print(f"The substring '{substring}' occurs {occurrences} times in the text.")

if __name__ == "__main__":
    main()
