# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title :Python function that takes a list of words and returns the length of the longest
# one

def find_longest_word_length(words):
    """
    Finds the length of the longest word in a list of words.

    Parameters:
    words (list): A list of strings, where each string is a word.

    Returns:
    int: The length of the longest word in the list. Returns 0 if the list is empty.
    """
    if not words:
        return 0
    longest_length = max(len(word) for word in words)
    return longest_length

def main():
    words = ["Prayag","Deven","Aditya","Shiv","Ayush"]
    longest_length = find_longest_word_length(words)
    print(f"The length of the longest word is: {longest_length}")

if __name__ == "__main__":
    main()
