# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title: Python program to find out the number of CPUs using

import os

def get_cpu_count():
    """
    Get the number of CPUs in the system.

    Returns:
    int: Number of CPUs
    """
    return os.cpu_count()

def main():

    cpu_count = get_cpu_count()
    print(f"The number of CPUs in this system is: {cpu_count}")

if __name__ == "__main__":
    main()
