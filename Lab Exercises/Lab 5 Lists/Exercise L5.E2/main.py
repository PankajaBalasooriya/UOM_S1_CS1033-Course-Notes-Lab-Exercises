# Prompt the user to enter the names of two sports, separated by a space and split it to a list sports
sports = input().split()

# Define the subjects and verbs
subjects = ["I", "We"]
verbs = ["play", "watch"]

# Generate and print sentences for each subject, verb, and sport combination using deep nested loops
for subject in subjects:
    for verb in verbs:
        for sport in sports:
            # Combine the subject, verb, and sport using string concatenation
            sentence = subject + " " + verb + " " + sport + "."
            # Print the statement
            print(sentence)