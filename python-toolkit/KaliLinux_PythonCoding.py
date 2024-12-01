import subprocess
import os
import pwd
import grp
import sys
import re
import ipaddress
from pathlib import Path
import nmap

def set_secure_permissions(path, user='root', group='root'):
    """
    Set secure permissions for a file or directory
    - 0o700 for files (owner read/write/execute only)
    - 0o750 for directories (owner full access, group read/execute)
    """
    try:
        path = Path(path)
        
        # Get user and group IDs
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(group).gr_gid
        
        # Set ownership
        os.chown(path, uid, gid)
        
        # Set permissions based on type
        if path.is_dir():
            os.chmod(path, 0o750)  # rwxr-x---
        else:
            os.chmod(path, 0o700)  # rwx------
            
        return True
    except Exception as e:
        print(f"Error setting permissions: {e}")
        return False

def create_secure_directory(directory_path, user='root', group='root'):
    """
    Create a directory with secure permissions
    """
    try:
        dir_path = Path(directory_path)
        
        # Create directory if it doesn't exist
        dir_path.mkdir(parents=True, exist_ok=True)
        
        # Set secure permissions
        return set_secure_permissions(dir_path, user, group)
    except Exception as e:
        print(f"Error creating secure directory: {e}")
        return False

def create_secure_file(file_path, user='root', group='root'):
    """
    Create a file with secure permissions
    """
    try:
        file_path = Path(file_path)
        
        # Create file if it doesn't exist
        file_path.touch(exist_ok=True)
        
        # Set secure permissions
        return set_secure_permissions(file_path, user, group)
    except Exception as e:
        print(f"Error creating secure file: {e}")
        return False

def check_root_privileges():
    """Check if script is running with root privileges"""
    if os.geteuid() != 0:
        print("This script requires root privileges to run.")
        print("Please run with sudo.")
        sys.exit(1)

def execute_command(command):
    """Execute command and return success status and output"""
    try:
        result = subprocess.run(
            command,
            shell=False,
            check=True,
            capture_output=True,
            text=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr
    except Exception as e:
        return False, str(e)

def check_tool_exists(tool_name):
    """Check if required tools are installed"""
    try:
        subprocess.run(['which', tool_name], 
                      check=True, 
                      capture_output=True, 
                      text=True)
        return True
    except subprocess.CalledProcessError:
        print(f"Error: {tool_name} is not installed. Please install it first.")
        return False

def validate_network_strict(network_str):
    """Strictly validate network string format"""
    try:
        # Validate it's a valid network address
        network = ipaddress.ip_network(network_str)
        
        # Additional validation to ensure only allowed characters
        if not re.match(r'^[\d./]+$', network_str):
            return False
        return True
    except ValueError:
        return False

def get_target_network():
    """Get and validate target network input"""
    while True:
        try:
            network = input("Enter target network (e.g., 192.168.1.0/24): ").strip()
            if validate_network_strict(network):
                return network
            print("Invalid network format. Please use CIDR notation.")
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            return None

def nmap_scan():
    """Nmap scanning function with permission checks"""
    try:
        # Check nmap permissions
        if not check_tool_exists('nmap'):
            print("Installing Nmap...")
            success, output = execute_command(['apt-get', 'install', '-y', 'nmap'])
            if not success:
                print(f"Failed to install Nmap: {output}")
                return None
            
        target_network = get_target_network()
        if not target_network:
            return None

        print("Running nmap scan...")
        
        # Create scanner with privilege check
        try:
            scanner = nmap.PortScanner()
        except nmap.PortScannerError:
            print("Nmap requires root privileges")
            return None
            
        print(f"Nmap Scanning network {target_network}...")
        
        # Perform the scan with service version detection
        scanner.scan(target_network, arguments='-sV -sS -O --version-intensity 5')
        
        # Process and display results
        for host in scanner.all_hosts():
            print(f"\nHost : {host}")
            print(f"State : {scanner[host].state()}")
            
            # Get OS information if available
            if 'osmatch' in scanner[host]:
                for os in scanner[host]['osmatch']:
                    print(f"OS Match: {os['name']} (Accuracy: {os['accuracy']}%)")
            
            # Get port information
            for proto in scanner[host].all_protocols():
                print(f"\nProtocol : {proto}")
                ports = scanner[host][proto].keys()
                
                for port in ports:
                    service = scanner[host][proto][port]
                    print(f"Port : {port}")
                    print(f"State : {service['state']}")
                    print(f"Service : {service['name']}")
                    if 'version' in service and service['version']:
                        print(f"Version : {service['version']}")
                    print("------------------------")
        
        return scanner
        
    except Exception as e:
        print(f"An unexpected error occurred during Nmap scan: {e}")
        return None

def bettercap_attack():
    """Bettercap attack function with permission checks"""
    try:
        # Check bettercap permissions
        if not check_tool_exists('bettercap'):
            print("Installing Bettercap...")
            success, output = execute_command(['apt-get', 'install', '-y', 'bettercap'])
            if not success:
                print(f"Failed to install Bettercap: {output}")
                return
            
        target_network = get_target_network()
        if not target_network:
            return
        
        if not validate_network_strict(target_network):
            print("Invalid network format or characters detected")
            return
        
        # Create caplet file for bettercap
        caplet_dir = Path("/tmp")
        caplet_file = caplet_dir / "attack.cap"
        
        # Write commands to caplet file
        caplet_content = f"""
set arp.spoof.fullduplex true
set arp.spoof.targets {target_network}
arp.spoof on
"""
        try:
            caplet_file.write_text(caplet_content)
            caplet_file.chmod(0o600)  # Secure file permissions
        except Exception as e:
            print(f"Failed to create caplet file: {e}")
            return
        
        print("Running bettercap attack...")
        print(f"Starting bettercap ARP spoofing attack on {target_network}...")
        
        # Updated command with correct flags
        cmd = [
            'bettercap',
            '-no-history',
            '-no-colors',
            '-caplet',
            str(caplet_file)
        ]
        
        try:
            result = subprocess.run(
                cmd,
                shell=False,
                check=True,
                capture_output=True,
                text=True
            )
            
            print("Attack completed.")
            return result.stdout
            
        except subprocess.CalledProcessError as e:
            print(f"Bettercap attack failed: {e}")
            print(f"Error output: {e.stderr}")
        finally:
            # Cleanup caplet file
            if caplet_file.exists():
                caplet_file.unlink()
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    finally:
        # Additional cleanup if needed
        pass


def install_metasploit_framework():
    """Install Metasploit Framework on Kali Linux"""
    try:
        print("\nInstalling Metasploit Framework on Kali Linux...")
        
        # Update package lists
        print("\nUpdating package lists...")
        success, output = execute_command(['apt-get', 'update'])
        if not success:
            print(f"Failed to update package lists: {output}")
            return False

        # Install curl if not present
        print("\nInstalling curl...")
        success, output = execute_command(['apt-get', 'install', '-y', 'curl'])
        if not success:
            print(f"Failed to install curl: {output}")
            return False

        # Download Metasploit installer
        print("\nDownloading Metasploit installer...")
        success, output = execute_command([
            'curl', 
            'https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb',
            '-o', 
            'msfinstall'
        ])
        if not success:
            print(f"Failed to download installer: {output}")
            return False

        # Make installer executable
        print("\nMaking installer executable...")
        success, output = execute_command(['chmod', '+x', 'msfinstall'])
        if not success:
            print(f"Failed to make installer executable: {output}")
            return False

        # Run installer
        print("\nRunning Metasploit installer...")
        success, output = execute_command(['./msfinstall'])
        if not success:
            print(f"Failed to run installer: {output}")
            return False

        # Initialize database
        print("\nInitializing Metasploit database...")
        success, output = execute_command(['msfdb', 'init'])
        if not success:
            print(f"Failed to initialize database: {output}")
            return False

        # Clean up installer
        print("\nCleaning up...")
        if os.path.exists('msfinstall'):
            os.remove('msfinstall')

        return True

    except Exception as e:
        print(f"An error occurred during installation: {e}")
        return False

def verify_installation():
    """Verify Metasploit Framework installation"""
    print("\nVerifying Metasploit Framework installation...")
    
    # Check if msfconsole exists
    success, output = execute_command(['which', 'msfconsole'])
    if not success:
        print("Metasploit Framework not found in PATH")
        return False

    # Check database status
    print("Checking database connection...")
    success, output = execute_command(['msfdb', 'status'])
    if not success:
        print(f"Database check failed: {output}")
        return False

    print("Metasploit Framework installation verified successfully!")
    return True

def metasploit_exploit():
    """Metasploit function with secure command execution"""
    try:
        # Check if Metasploit is installed
        if not check_tool_exists('msfconsole'):
            print("Metasploit Framework not found. Installing...")
            if not install_metasploit_framework():
                print("Failed to install Metasploit Framework")
                return
            if not verify_installation():
                print("Metasploit installation verification failed")
                return

        # Start PostgreSQL service
        print("\nStarting PostgreSQL service...")
        success, output = execute_command(['service', 'postgresql', 'start'])
        if not success:
            print(f"Failed to start PostgreSQL: {output}")
            return

        # Initialize database if needed
        print("\nChecking database status...")
        success, output = execute_command(['msfdb', 'status'])
        if not success:
            print("Initializing Metasploit database...")
            success, output = execute_command(['msfdb', 'init'])
            if not success:
                print(f"Failed to initialize database: {output}")
                return

        target_network = get_target_network()
        if not target_network:
            return

        # Create resource file for Metasploit commands
        resource_file = Path('/tmp/msf_commands.rc')
        try:
            resource_file.write_text(
                f"db_connect\n"
                f"db_nmap -sV {target_network}\n"
            )
           # Set secure permissions for resource file
            set_secure_permissions(resource_file, 'root', 'root')
        except Exception as e:
            print(f"Failed to create resource file: {e}")
            return

        try:
            # Execute Metasploit
            print("\nStarting Metasploit Framework...")
            success, output = execute_command([
                'msfconsole',
                '-q',
                '-r',
                str(resource_file)
            ])
            if not success:
                print(f"Metasploit execution failed: {output}")
            else:
                print(output)

        finally:
            # Cleanup
            if resource_file.exists():
                resource_file.unlink()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Stop PostgreSQL service
        execute_command(['service', 'postgresql', 'stop'])

def main_menu():
    """Main menu with initial permission setup"""
    try:
        # Check root privileges
        check_root_privileges()
        
        while True:
            print("\n=== Security Testing Tool ===")
            print("1. Run Nmap Scan")
            print("2. Run Bettercap Attack")
            print("3. Run Metasploit Exploit")
            print("4. Install Metasploit Framework")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == '1':
                nmap_scan()
            elif choice == '2':
                bettercap_attack()
            elif choice == '3':
                metasploit_exploit()
            elif choice == '4':
                if install_metasploit_framework():
                    verify_installation()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nExiting due to user interrupt...")
        sys.exit(0)

if __name__ == "__main__":
    main_menu()
