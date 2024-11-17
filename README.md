# Advanced Port Scanner

The **Advanced Port Scanner** is a Python-based tool leveraging Nmap to identify open ports and detect potential vulnerabilities on a target system. Designed for cybersecurity professionals, it simplifies network audits and enhances system security.

---

## Features
- Scans open ports on a target system.
- Detects service versions running on open ports using Nmap.
- Lightweight and easy to use.
- Ideal for network security audits.

---

## Requirements
- **Python 3**: Ensure Python is installed on your system.
- **Nmap**: The scanner relies on Nmap for detecting ports and services.

---

## Installation
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
2. Ensure Nmap is installed on your system
   sudo apt install nmap

---

## Example Usage
1. To scan a target IP (e.g., 192.168.1.1) for open ports: python3 port_scanner.py --target 192.168.1.1
2. Sample output:
Scanning target: 192.168.1.1
Port 22: Open (SSH)
Port 80: Open (HTTP)
Port 443: Open (HTTPS)

---

## Limitations
1. Requires Nmap to be installed and operational.
2. Designed for use in a controlled environment (e.g., your own network or with proper authorization).
3. Scans may take longer on networks with high latency or many open ports.

---

## Disclaimer
This tool is intended for educational purposes and authorized network security testing only. Unauthorized use on networks you do not own or have explicit permission to test is illegal and unethical. The authors are not responsible for misuse.

## License
No license has been applied to this project. Usage, modification, or redistribution of the code requires explicit permission from the author.
