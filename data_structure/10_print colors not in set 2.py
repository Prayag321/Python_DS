# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title: Python program to print out a set containing all the colors from color_list_1 which
#are not present in color_list_2.

def get_unique_colors(color_list_1, color_list_2):
    """
    Get a set of colors that are in color_list_1 but not in color_list_2.

    Parameters:
    color_list_1 (set): First set of colors
    color_list_2 (set): Second set of colors

    Returns:
    set: A set of colors that are in color_list_1 but not in color_list_2
    """
    return color_list_1 - color_list_2

def main():
    color_list_1 = {"White", "Black", "Red"}
    color_list_2 = {"Red", "Green"}
    
    unique_colors = get_unique_colors(color_list_1, color_list_2)
    print("Colors in color_list_1 not in color_list_2:", unique_colors)

if __name__ == "__main__":
    main()
