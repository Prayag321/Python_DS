"""
    @Author: Prayag Bhoir
    @Date: 26-07-2024
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 26-07-2024
    @Title : Python program to create a vertical histogram from a given list of integers.
"""

def vertical_histogram(items):
    """
    Description:
        This function prints a vertical histogram from a given list of integers.
    Parameters:
        items: list of integers
    Returns:
        None
    """
    if not items:
        print("No data to display.")
        return

    max_value = max(items)
    
    # Iterate from the top of the histogram to the bottom
    for level in range(max_value, 0, -1):
        line = ''
        for n in items:
            if n >= level:
                line += '* '
            else:
                line += '  '
        print(line)

def main():
    items = [1, 14, 5]
    vertical_histogram(items)

if __name__ == "__main__":
    main()
