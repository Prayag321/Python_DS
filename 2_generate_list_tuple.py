"""
    @Author:Prayag Bhoir
    @Date: 26-7-24
    @Last Modified time: 26-07-2024 14:00:00
    @Title : Python program to  generate a list and a tuple with user numbers.
"""
def generate_list_and_tuple(input_data):
    """
    Description:
        This function accepts a sequence of comma-separated numbers from the user and generates a list and a tuple with those numbers.
    Parameters:
        None
    Returns:
        list: A list of the input numbers as strings.
        tuple: A tuple of the input numbers as strings.
    """
    number_list = input_data.split(",")
    number_tuple = tuple(number_list)
    
    return number_list, number_tuple

def main():
    input_data = input("Please enter a sequence of comma-separated numbers: ")
    number_list, number_tuple = generate_list_and_tuple(input_data)
    print("List :", number_list)
    print("Tuple:", number_tuple)

# Call the main function
if __name__ == "__main__":
    main()
