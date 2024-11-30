import sys

def option_one():
    print("You selected Option One!")

def option_two():
    print("You selected Option Two!")

def option_three():
    print("You selected Option Three!")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <option>")
        print("Options: one, two, three")
        sys.exit(1)

    option = sys.argv[1]

    if option == "one":
        option_one()
    elif option == "two":
        option_two()
    elif option == "three":
        option_three()
    else:
        print(f"Invalid option: {option}")
        print("Options: one, two, three")
        sys.exit(1)

if __name__ == "__main__":
    main()
