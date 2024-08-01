# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title : Write a Python program that accepts a comma separated sequence of words as input
# and prints the unique words in sorted form (alphanumerically).
def get_unique_sorted_words(words):
    """
    Returns a sorted list of unique words from a comma-separated sequence.

    Parameters:
    words (str): A comma-separated string of words.

    Returns:
    unique_words(list): A sorted list of unique words.
    """
    word_list = words.split(',')
    unique_words = list(set(word_list))
    unique_words.sort()
    return unique_words

def main():
    user_input = input("Please enter a comma-separated sequence of words: ")
    unique_sorted_words = get_unique_sorted_words(user_input)
    print("Expected Result:"," ".join(unique_sorted_words))

if __name__ == "__main__":
    main()
