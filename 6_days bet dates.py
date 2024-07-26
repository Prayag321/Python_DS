from datetime import date

# @Author: Prayag Bhoir
# @Date: 26-7-24
# @Last Modified time: 26-07-2024 14:00:00
# @Title : Python program to calculate number of days between two dates

def calculate_days_between_dates(date1, date2):
    """
    Description:
        This function calculates the number of days between two given dates.
    Parameters:
        date1 (tuple): The first date as a tuple (year, month, day).
        date2 (tuple): The second date as a tuple (year, month, day).
    Returns:
        int: The number of days between the two dates.
    """
    # Convert tuples to date objects
    d1 = date(*date1)
    d2 = date(*date2)
    
    # Calculate the difference between the dates
    delta = d2 - d1
    
    # Return the number of days as an integer
    return abs(delta.days)

def main():

    # Sample dates
    date1 = (2014, 7, 2)
    date2 = (2014, 7, 11)
    

    number_of_days = calculate_days_between_dates(date1, date2)

    print(f"The number of days between {date1} and {date2} is: {number_of_days} days")

if __name__ == "__main__":
    main()
