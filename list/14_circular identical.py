'''
    @Author: Prayag Bhoir
    @Date: 01-08-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 01-08-2024 
    @Title : Python program to check whether two lists are circularly identical
'''

def circularly_identical(list1, list2):
    """
    Description:
        This function checks if two lists are circularly identical.
    Parameters:
        list1 : list of elements
        list2 : list of elements
    Return:
        bool : True /False 
    """
    if len(list1) != len(list2):
        return False
        
    doubled_list1 = list1 + list1

    for i in range(len(list1)):
        if doubled_list1[i:i+len(list2)] == list2:
            return True
    
    return False

def main():

    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 1, 2]

    result = circularly_identical(list1, list2)
    
    if result:
        print("The lists are circularly identical.")
    else:
        print("The lists are not circularly identical.")

if __name__ == "__main__":
    main()
