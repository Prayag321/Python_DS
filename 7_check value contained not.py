# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title : Python program to check whether a specified value is contained in a group of values

def is_value_in_list(value, value_list):
    """
    Description:
        This function checks whether a specified value is contained in a given list of values.
    Parameters:
        value (int): The value to check for in the list.
        value_list (list): The list of values to check against.
    Returns:
        bool: True if the value is in the list, False otherwise.
    """
    return value in value_list

def main():
    test_value_1 = 3 #test
    test_list_1 = [1, 5, 8, 3]

    result_1 = is_value_in_list(test_value_1, test_list_1)
   
    print(f"{test_value_1} -> {test_list_1} : {result_1}")


if __name__ == "__main__":
    main()