"""
    @Author:Prayag Bhoir
    @Date: 26-7-24
    @Last Modified time: 26-07-2024 14:00:00
    @Title : Python program to  print first and last colors from givern list
  """
def get_first_and_last_colors(color_list):
    """
    Description:
        This function returns the first and last colors from the provided color list.
    Parameters:
        color_list (list): A list of colors.
    Returns:
        tuple: A tuple containing the first and last colors.
    """
    first_color = color_list[0]
    last_color = color_list[-1]
    return first_color, last_color

def main():
    color_list = ["Red", "Green", "White", "Black"]
    first_color, last_color = get_first_and_last_colors(color_list)
    print("color list :",color_list)
    print("First color:", first_color)
    print("Last color:", last_color)


if __name__ == "__main__":
    main()
