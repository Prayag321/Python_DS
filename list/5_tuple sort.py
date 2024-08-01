'''
    @Author: Prayag bhoir
    @Date: 01-08-2024 
    @Last Modified by: Prayag bhoir
    @Last Modified time: 01-08-2024 
    @Title : Python program to sort a list of tuples by the last element in each tuple
'''

def sort_tuples_by_last_element(tuples_list):
    """
    Description:
        This function sorts a tuple in increasing order by the last element in each tuple.
    Parameters:
        tuples_list : list of tuple
    Return:
        list : sorted list of tuples
    """
    return sorted(tuples_list, key=lambda x: x[len(x)-1])

def main():
    sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    sorted_list = sort_tuples_by_last_element(sample_list)
    
    print("Original List:", sample_list)
    print("Sorted List:", sorted_list)

if __name__ == "__main__":
    main()
