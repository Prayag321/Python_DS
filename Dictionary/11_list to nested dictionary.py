"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 30-07-2024 
    @Title : Python program  to convert a list into a nested dictionary of keys
"""
def list_to_nested_dict(input_list):
    """
    Converts a list into a nested dictionary of keys.

    Parameters:
    input_list (list): A list of elements

    Returns:
    dict: A nested dictionary 
    """
    nested_dict = current_level = {}
    for element in input_list:
        current_level[element] = {}
        current_level = current_level[element]
    return nested_dict

def main():
    sample_list = ["a", "b", "c", "d"]
    nested_dict = list_to_nested_dict(sample_list)
    print("Nested dictionary:", nested_dict)

# Execute the main function
if __name__ == "__main__":
    main()
