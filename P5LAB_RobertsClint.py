def days_in_feb(user_year):
    # Check if the year is divisible by 4
    if user_year % 4 == 0:
        # If it is a century year
        if user_year % 100 == 0:
            # Check if it is divisible by 400
            if user_year % 400 == 0:
                # If it is divisible by 400, it is a leap year, so February has 29 days
                return 29
            else:
                # If it is not divisible by 400, it is not a leap year, so February has 28 days
                return 28
        else:
            # If it is not a century year but divisible by 4, it is a leap year, so February has 29 days
            return 29
    else:
        # If it is not divisible by 4, it is not a leap year, so February has 28 days
        return 28

if __name__ == '__main__':
    # Take input year from user
    user_year = int(input().strip())
    # Call days_in_feb function to get number of days in February for input year
    days = days_in_feb(user_year)
    # Print the result
    print(f"{user_year} has {days} days in February.")
