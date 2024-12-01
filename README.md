# HackFD 2024

HackFD 2024 is the _Canadian Army's_ first annual Hackathon. This repository contains team _Scarlet Shields_ project submission, the _Scarlet Sword_.

> A _Hackathon_ is an event where people engage in rapid and collaborative engineering over a relatively short period of time such as 24 or 48 hours. It's origin is a combination of "hack" and "marathon", where "hack" is used in the sense of exploratory programming.

## Table of Contents
- [Team Scarlet Sheilds](#team-scarlet-sheilds)
  - [Team Members](#team-members)
- [Project Scarlet Sword](#project-scarlet-sword)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Roadmap](#roadmap)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)
  - [Disclaimer](#disclaimer)
 
# Team Scarlet Sheilds

The _Scarlet Sheilds_ is _5th Canadian Division's_ Team 1 submission to the _Canadian Army's_ HackFd 2024.

## Team Members

- Capt Johnny Woodgate
- Cpl Ben Hovinga
- Cpl Dominick Goertzen
- Cpl Hugo Chiasson

# Project Scarlet Sword

A security testing suite prioritizing quick and efficient execution of common open source ITSec tools. In this itteration of the HackFD idea we use Nmap, Bettercap, and Metasploit functionalities.

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
- Advanced reporting and logging features
- Automated testing capabilities
- Configuration management dashboard

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2024 Dominick Goertzen, Ben Hovinga, Johnny Woodgate, Hugo Chiasson

## Acknowledgments

- [Python Project](https://www.python.org/)
- [Nmap Project](https://nmap.org/)
- [Bettercap Project](https://www.bettercap.org/)
- [Metasploit Framework](https://www.metasploit.com/)

## Disclaimer

This tool is for educational and authorized testing purposes only. Users are responsible for obtaining proper authorization before testing any networks or systems.
