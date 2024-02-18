from datetime import datetime
#from cs1033_evaluator import evaluate_lab7


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

# assigning file name to a variable
input_file_name = input()
years = []
# Creating input dile object to read from the file
# with open(input_file_name, "r") as input_file:
input_file = open(input_file_name, "r")
output_file = open("output.txt", "w")
for record in input_file:
    row = record.split()
    name = row[0]
    birthday = row[1]
    gender = row[2]
    year = str(birthday[0:4])
    years.append(year)
    day = days_to_birthday(birthday)
    if gender == "F":
        day += 500
    day = str(day)
    if len(day) == 1:
        day = "00" + day
    if len(day) == 2:
        day = "0" + day
    num = 0
    for yearinList in years:
        if yearinList == year:
            num = num + 1
    num = str(num)
    # generating last 3 digits
    if len(num) == 1:
        number = "00" + num
    if len(num) == 2:
        number = "0" + num

    output_file.write(name + " " + year + day + number + "\n")
output_file.close()

################################################################################
# Please do not edit anything below this line.
#evaluate_lab7()

##################### End of the programme #####################################