# Docstrings
def days_in_month(year, month):
    # Docstrings, 3x " " so it adds extra info about the function
    """Take month entered as 1 through 12 and return the number of 
    days in the month, including leap years."""
    if month > 12 or month <1:
        return "Invalid month, enter value between 1 and 12."
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        if is_leap(year) == True:
            return 29
        else:
            return month_days[month - 1] 

days_in_month()