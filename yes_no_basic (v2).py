
# Functions go here
def yes_no(question):

    """Checks user response to a question is a yes / no (y/n), returns 'yes' or 'no' """
    while True:

        response =input(question).lower()
        # check if the user says yes or no
        if response == "yes" or response == "y":
            return "yes"
            break
        elif response == "no" or response== "n":
            return "no"
            break
        else:
            print("please enter yes or no")
            continue

# Main Routine

want_instructions = yes_no("Do you want to see the instructions? ")

print("we done")
