# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title : Python program to display formatted text (width=50) as output
import textwrap

def format_text(input_text, width=50):
    """
    Formats the given text to the specified width.

    Parameters:
    input_text (str): The text to be formatted.
    width (int): The width to format the text to. Default is 50.

    Returns:
    wrapped_text (str): The formatted text.
    """
    wrapped_text = textwrap.fill(input_text, width=width)
    return wrapped_text

def main():
    input_text = input("Please enter the text to be formatted: ")
    formatted_text = format_text(input_text)
    print("\nFormatted text:\n")
    print(formatted_text)

if __name__ == "__main__":
    main()
  
