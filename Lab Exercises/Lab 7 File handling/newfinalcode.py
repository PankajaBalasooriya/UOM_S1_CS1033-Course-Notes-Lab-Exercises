from datetime import datetime
from cs1033_evaluator import evaluate_lab7


def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Please do not edit anything above this line.
################################################################################
def add_padding(numb):
    '''Add padding to a number by adding zeros if the number has less than three digits.'''
    if len(numb) == 1:
        numb = "00" + numb
    if len(numb) == 2:
        numb = "0" + numb
    return numb


# Read the input file name from the user
input_file_name = input()
years = []

# Open the input file for reading
with open(input_file_name, "r") as input_file:
    # Open the output file for writing
    with open("output.txt", "w") as output_file:
        # Read each line in the input file
        for record in input_file:
            # Split the record into a list
            row = record.split()

            # Split the row list into name, birthday, and gender
            name, birthday, gender = row[0], row[1], row[2]

            # Get the birth year from the birthday
            birth_year = str(birthday[0:4])

            # Add the year to the years list
            years.append(birth_year)

            # Calculate the number of days to the birth date
            day = days_to_birthday(birthday)

            # Add 500 days if the gender is female
            if gender == "F":
                day += 500
            day = str(day)

            # Padding the day with zeros if necessary
            day = add_padding(day)

            # Count the number of occurrences of the current year in the years list
            count = 0
            for year in years:
                if year == birth_year:
                    count = count + 1
            last_digit = str(count)

            # Padding the last numbers with zeros if necessary
            last_digits = add_padding(last_digit)

            # Write the name and NIC number to the output file after concatanationg the NIC number
            output_file.write(name + " " + birth_year + day + last_digits + "\n")

################################################################################
# Please do not edit anything below this line.
evaluate_lab7()

##################### End of the programme #####################################