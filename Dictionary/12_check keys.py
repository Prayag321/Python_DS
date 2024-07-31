"""
    @Author: Prayag Bhoir
    @Date: 31-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 31-07-2024 
    @Title : Python program to check multiple keys exists in a dictionary
"""

def check_keys_exist(dictionary, keys):
    """
    Description:
      This function checks if multiple keys exist in a dictionary

    Parameters:
      dictionary (dict): The dictionary 
      keys (list): A list of keys 

    Returns:
      bool: True if all keys exist, False otherwise.
    """
    return all(key in dictionary for key in keys) #its iteratable and check all true

def main():
    sample_dict = {"a": 1, "b": 2, "c": 3}
    keys_to_check = ["a", "b"]
    result = check_keys_exist(sample_dict, keys_to_check)
    print("Do all keys exist?", result)


if __name__ == "__main__":
    main()
