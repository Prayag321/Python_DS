'''
    @Author: Prayag bhoir
    @Date: 01-08-2024 
    @Last Modified by: Prayag bhoir
    @Last Modified time: 01-08-2024 
    @Title : Python program to generate all permutations of a list without using inbuilt methods
'''

def permute(lst):
    """
    Description:
        This function generates all permutations of a list.
    Parameters:
        lst : list of elements
    Return:
        list : list of all permutations
    """
    if len(lst) == 0:
        return []
    
    if len(lst) == 1:
        return [lst]
    
    perms = []  # list to store current permutations
    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i] + lst[i+1:]
        
        for p in permute(remaining):
            perms.append([current] + p)
    
    return perms

def main():
    sample_list = [1, 2, 3]
    all_perms = permute(sample_list)
    
    print("Original List:", sample_list)
    print("All Permutations:")
    for perm in all_perms:
        print(perm)

if __name__ == "__main__":
    main()
