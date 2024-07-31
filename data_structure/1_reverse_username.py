    # @Author:Prayag Bhoir
    # @Date: 26-7-24
    # @Last Modified time: 26-07-2024 14:00:00
    # @Title : Python program to reverse the user name

def reverse_name(first_name,last_name):
    """
    Description:
        This function accepts the user's first and last name and prints them in reverse order with a space between them.
    Parameters:
        None
    Returns:
        None
    """
    return f"{last_name} {first_name}"

# Call the function
def main():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    print("Reverce order is :",reverse_name(first_name,last_name))

if __name__=="__main__":
    main()