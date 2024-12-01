import sys
from KaliLinux_PythonCoding import nmap_scan, bettercap_attack, metasploit_exploit

def option_one():
    print("You selected Option One!")
    nmap_scan()

def option_two():
    print("You selected Option Two!")
    bettercap_attack()

def option_three():
    print("You selected Option Three!")
    metasploit_exploit()
    
def option_four():
    print("You selected Option Four!")
    print("Exiting the program.")
    sys.exit(0) 
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <option>")
        print("Options: one(Nmap Scan), two(Bettercap Attack), three (Metasploit Exploit), four (Exit)")
        sys.exit(1)

    option = sys.argv[1]

    options = {
        "one": option_one,
        "two": option_two,
        "three": option_three,
        "four": option_four
    }

    if option in options:
        options[option]()
    else:
        print(f"Invalid option: {option}")
        print("Options: one (Nmap Scan), two (Bettercap Attack), three (Metasploit Exploit), four (Exit)")
        sys.exit(1)

if __name__ == "__main__":
    main()