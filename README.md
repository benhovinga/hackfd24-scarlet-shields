# HackFD 2024 - Team Scarlet Shields

HackFD 2024 is the Canadian Army's first annual Hackathon. This repository is team _Scarlet Shields_ project submission.

## Description
# Security Testing Tool

A comprehensive security testing tool built in Python that integrates Nmap, Bettercap, and Metasploit functionalities with secure implementation and proper error handling.

## Description

This tool provides a command-line interface for common security testing operations, including:
- Network scanning with Nmap
- Network attacks with Bettercap
- Exploit execution with Metasploit Framework

The tool is built with security in mind, implementing:
- Full path execution
- Input validation
- Proper error handling
- Secure command execution
- Comprehensive logging
- Resource cleanup

## Prerequisites

### Required Software
- Python 3.8+
- Nmap
- Bettercap
- Metasploit Framework

### Installation

1. Install required system packages:
```bash
sudo apt update
sudo apt install -y nmap bettercap metasploit-framework

2. Clone the repository:
git clone https://github.com/yourusername/security-testing-tool.git
cd security-testing-tool

3. Setup Python virtual environment
python -m venv venv
source venv/bin/activate

4. Install Python dependencie
pip install -r requirements.txt

### Usage
Run the tool with root privileges: sudo python main.py

### Main Menu Options
1. Nmap Scan

Performs network scanning

Requires target IP/network

Displays service version information

2. Bettercap Attack

Executes ARP spoofing attacks

Requires target network in CIDR notation

Includes safety checks and cleanup

3. Metasploit Exploit

Runs Metasploit exploits

Requires target IP and exploit path

Includes session management and cleanup

4. Exit

Safely exits the programs

Perform cleanup operation

### Security Features
## Input Validation
IP address validation

CIDR notation validation

Exploit path validation

Command injection prevention

## Error Handling

Specific exception types

Custom error classes

Comprehensive logging

Proper error recovery

## Security Measures

Full path execution

No shell injection possibilities

Privilege management

Resource cleanup

Session management

### Logging

Logs are stored in the logs directory with the following information:

Timestamp

Operation type

Success/failure status

Error messages

Stack traces for debugging

### Error Handling

The tool implements proper error handling for:

File not found errors

Permission errors

Validation errors

Execution errors

Network errors

User interrupts

### Contributing 

1. Fork the repository

2. Create your feature branch: git checkout -b feature/YourFeature

3. Commit your changes: git commit -m 'Add some feature'

4. Push to the branch: git push origin feature/YourFeature

5. Create a Pull Request

### Security Consideration

Run with appropriate permissions

Review target scope before scanning

Follow security best practices

Monitor system resources

Review logs regularly

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

Nmap Project

Bettercap Project

Metasploit Framework

Python Security Community

### Disclaimer

This tool is for educational and authorized testing purposes only. Users are responsible for obtaining proper authorization before testing any networks or systems.

### Support

For support, please: 

1. Check the documentation

2. Review closed issues

3. Open a new issue with : 

Clear description

Steps to reproduce

Expected behavior

Logs/error messages

### Roadmap

Future improvements planned:

GUI interface

Additional security tools integration

Advanced reporting features

Automated testing capabilities

Configuration management


This README.md provides:
- Clear project description
- Installation instructions
- Usage guidelines
- Security features
- Contributing guidelines
- Support information
- Future plans

Remember to:
- Keep it updated
- Add specific examples
- Include screenshots if needed
- Update security warnings
- Maintain documentation


