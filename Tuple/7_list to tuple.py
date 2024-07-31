"""
    @Author: Prayag Bhoir
    @Date: 29-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 29-07-2024 
    @Title : Python program to convert a list to a tuple.
"""

def list_to_tuple(lst):
    """
    Description:
      Converts a list to a tuple.

    Parameters:
      lst (list): list of elements.

    Returns:
      tuple: tuple containing the elements of the list.
    """
    return tuple(lst)

def main():
    sample_list = [1, 2, 3, 4, 5, 6]
    result_tuple = list_to_tuple(sample_list)
    print(f"List: {sample_list}\nConverted Tuple: {result_tuple}")

if __name__ == "__main__":
    main()
