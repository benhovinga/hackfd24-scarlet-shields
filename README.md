# HackFD 2024 - Team Scarlet Shields

HackFD 2024 is the Canadian Army's first annual Hackathon. This repository is team _Scarlet Shields_ project submission.

# Project Scarlet Sword

A comprehensive security testing tool built in Python that integrates Nmap, Bettercap, and Metasploit functionalities with secure implementation and proper error handling.

This tool provides a command-line interface for common security testing operations, including:

- Network scanning with Nmap
- Network attacks with Bettercap
- Exploit execution with Metasploit Framework

## Prerequisites

- Python 3.12+
- Nmap
- Bettercap
- Metasploit Framework

## Installation

1. Install required system packages

```bash
sudo apt update
sudo apt install -y nmap bettercap metasploit-framework
```

2. Clone the repository

```bash
git clone https://github.com/benhovinga/hackfd24-scarlet-shields.git
cd hackfd24-scarlet-shields
```

3. Setup Python virtual environment

```bash
cd python-toolkit
python3 -m venv .venv
source .venv/bin/activate
```

4. Install Python dependencies

```bash
pip3 install -r requirements.txt
```

## Usage

Run the tool with root privileges

```bash
sudo python3 scarlet-sword.py
```

### Main Menu Options

```text
=== Security Testing Tool ===
1. Run Nmap Scan
2. Run Bettercap Attack
3. Run Metasploit Exploit
4. Install Metasploit Framework
5. Exit
```

## Roadmap

Future improvements that may be implemented:

- GUI interface (WIP)
- Additional security tools integration
- Advanced reporting features
- Automated testing capabilities
- Configuration management

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2024 Ben Hovinga, Dominick Goertzen, Hugo Chiasson, Johnny Woodgate

## Acknowledgments

- [Nmap Project](https://nmap.org/)
- [Bettercap Project](https://www.bettercap.org/)
- [Metasploit Framework](https://www.metasploit.com/)

## Disclaimer

This tool is for educational and authorized testing purposes only. Users are responsible for obtaining proper authorization before testing any networks or systems.
