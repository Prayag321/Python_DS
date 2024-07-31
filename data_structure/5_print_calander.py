"""
    @Author:Prayag Bhoir
    @Date: 26-7-24
    @Last Modified time: 26-07-2024 14:00:00
    @Title : Python program to print month calander as per user month and year
"""
import calendar

def print_calendar(year, month):
    """
    Description:
        This function prints the calendar for a given month and year.
    Parameters:
        year (int): The year for which the calendar is to be printed.
        month (int): The month for which the calendar is to be printed.
    Returns:
        cal
    """
    cal = calendar.month(year, month)
    return (cal)

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    print(f"The month calander is :\n {print_calendar(year, month)}")


if __name__ == "__main__":
    main()
