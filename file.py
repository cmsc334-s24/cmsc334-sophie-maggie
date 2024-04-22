# Function to append text to an existing file entry
def append_entry():
    name = get_file_name()
    filename = name + ".txt"

    with open(filename, "a") as file_management_system:
        print(f"Type your file content for {name} (Enter END on a new line when done.):")
        while True:
            line = input()
            if line == "END":
                break
            file_management_system.write(line + "\n")


# Function to create a new file entry
def create_entry():
    name = get_file_name()
    filename = name + ".txt"

    print(f"Type your file content for {name} (Enter END on a new line when done.):")
    with open(filename, "w") as file_management_system:
        while True:
            line = input()
            if line == "END":
                break
            file_management_system.write(line + "\n")


# Function to read an entry file and print that file to the terminal
def read_entry():
    name = get_file_name()
    filename = name + ".txt"

    try:
        with open(filename, "r") as file_management_system:
            for line in file_management_system:
                print(line.rstrip())
    except FileNotFoundError:
        print(f"Could not find file entry for {name}")


def get_file_name():
    name = input("Please enter the file name without white spaces: ")
    return name


if __name__ == "__main__":
    print("Welcome to the File Management System!")

    # While loop for operations, run until exit or End-Of-File (EOF)
    while True:
        print("\nChoose an operation:")
        print("(x) : Exit")
        print("(n) : Create a new file")
        print("(r) : Read a file")
        print("(a) : Append to an existing file")

        choice = input()

        # Check if the user wants to exit
        if choice == 'x':
            # Return from program
            break

        switcher = {
            'n': create_entry,
            'r': read_entry,
            'a': append_entry
        }

        # Get the function from switcher dictionary
        func = switcher.get(choice, lambda: print("ERROR: Invalid input. Choose again."))

        # Execute the function
        func()
