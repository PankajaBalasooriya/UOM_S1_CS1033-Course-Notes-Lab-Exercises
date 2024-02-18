# creating a 2D list to store the marks of 4 students
marks = [[] for x in range(0, 4)]

# Input marks for each student
for student in range(0, 4):
    # Get input marks for a student as a list of integers
    marks_list = list(map(int, input().split()))
    # store the marks in the 2D list
    marks[student] = marks_list

# Calculate and display total and average marks for each student
for student in range(0, 4):
    total = 0
    # Calculate total marks of each student
    for subject in range(0, 3):
        total += marks[student][subject]
    # Calculate the average of each student
    average = total / 3
    # Display the total and average marks for the student
    print(f"Total: {int(total)} Average: {average:.1f}")
