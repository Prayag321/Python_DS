# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title : Python program to calculate the length of a string

def main():
    user_string = input("Enter a string: ")
    print(f"The length of the string is: {sum([1 for char in user_string])}")

if __name__ == "__main__":
    main()