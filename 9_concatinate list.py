# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024
# @Title: Python program to check whether a specified value is contained in a group of values

def concatenate_elements(input_list):
    """
    Description:
      Concatenate all elements in a list into a string.

    Parameters:
      input_list (list): List of elements to concatenate

    Returns:
      str: A string with all the elements concatenated
    """
    joined_string=""
    for elem in input_list:
      joined_string+=elem
    return joined_string

def main():
    sample_list = ['Hello', ' ', 'world', '!', ' ', 'This', ' ', 'is', ' ', 'Python', '.']
    result = concatenate_elements(sample_list)
    print(result) 

if __name__ == "__main__":
    main()
