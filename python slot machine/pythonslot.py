MAX_LINES = 3  # a constant value it is called a global constant
MAX_BET = 100
MIN_BET = 1

# Need to test: passed


def deposit():  # wrote a function deposit
    while True:  # while loop to continue till break
        amount = input("What would you like to deposit? $")  # question
        if amount.isdigit():  # something, if a digit, go to amount = int(amount)
            # if above is a number it will get converted to a integer
            amount = int(amount)
            if amount > 0:  # if geater than zero it will break out
                break  # this just ends the while loop
            else:
                # if it is not greater than zero it will let the user know and they will have to input a number gearter than 0
                print("Amount must be greater than 0.")
        else:
            # if not a number it will ask for a number to be entered
            print("Please enter a number.")

        return amount


# now this is a deposit function
def get_number_of_lines():  # using _ to space out my varible
    while True:
        # I changed amount with lines and implement the global constant in this string
        lines = input(
            "Enter the Number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)  # lines should equal a int
            if 1 <= lines <= MAX_LINES:  # to check if a value is between two values
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
            return lines


def


def main():  # I will make a main function in case I want to recall this function at a later point
    balance = deposit()
    lines = get_number_of_lines()
    # just to see what the above is when you run the program
    print(balance, lines)


main()  # call main function so you start running main #goal to collect bet from user
