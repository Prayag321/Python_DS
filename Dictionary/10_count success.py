"""
    @Author: Prayag Bhoir
    @Date: 30-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 31-07-2024 
    @Title : Python program to count the values associated with key in a
dictionary.
"""
def count_success(dict_list):
    """
    Description:
      Counts 'success' is True.

    Parameters:
      dict_list (list): A list of dictionaries.

    Returns:
      int: The count od success
    """
    count = 0
    for dictionary in dict_list:
        if dictionary['success'] == True:
            count += 1
    return count

def main():

    data = [
        {'id': 1, 'success': True, 'name': 'Prayag'},
        {'id': 2, 'success': False, 'name': 'Ayush'},
        {'id': 3, 'success': True, 'name': 'Shiv'}
    ] 
    success_count = count_success(data)
    print(f"Count of dictionaries with success as True: {success_count}")

if __name__ == "__main__":
    main()
