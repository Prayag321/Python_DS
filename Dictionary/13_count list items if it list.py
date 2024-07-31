"""
    @Author: Prayag Bhoir
    @Date: 31-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 31-07-2024 
    @Title : Python program to count number of items in a dictionary value that is a list
"""

def count_items_in_list_values(dictionary):
    """
    Description:
      Counts the number of items in a dictionary value that is a list.

    Parameters:
      dictionary (dict): The dictionary with list values.

    Returns:
      dict: A dictionary with the same keys and the count of items in values.
    """
    return {key: len(value) for key, value in dictionary.items() if isinstance(value, list)}

def main():
    sample_dict = {
        "a": [1, 2, 3],
        "b": [4, 5],
        "c": "not a list",
        "d": [6, 7, 8, 9]
    }
    result = count_items_in_list_values(sample_dict)
    print("Count of items in list values:", result)


if __name__ == "__main__":
    main()
