
def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


if __name__ == "__main__":
    print("This is not a program, Try importing and using the classes")
    input("\n\n Press Enter to Exit")