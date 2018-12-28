import short


def user_interface():
    """
    This function will create a user and ask for users to enter in commands
    :return:
    """

    user = short.Short()

    while True:

        # prints available commands and requests user command
        print("Available commands are:\n")
        print("quit -> quit program\n long -> convert long to short\n short -> convert short to long \n")
        command = input("What would you like to do?\n")

        if command == "quit":
            print("Goodbye")
            break

        elif command == "long":
            url = input("Please enter your url: ")
            print("Long: " + user.convert_large_to_short(url))

        elif command == "short":
            url = input("Please enter your url: ")
            print("Short: " + user.convert_short_to_large(url))

        else:
            print("Invalid command, please try again")


if __name__ == '__main__':
    user_interface()
