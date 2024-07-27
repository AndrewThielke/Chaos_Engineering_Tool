# Wifi_Vulnerability_Scanner

## Overview

The **Wifi_Vulnerability_Scanner** is a Python-based tool designed to scan and list vulnerabilities for devices connected to a WiFi network. This tool identifies devices, detects open ports and services, assesses operating systems, and checks for known vulnerabilities. It provides a comprehensive report to help network administrators and security enthusiasts ensure the security and resilience of their networks.

## Disclaimer

This tool is intended for educational and research purposes only. Unauthorized network scanning is illegal and unethical. Always obtain explicit permission from network owners before using this tool. The author is not responsible for any misuse of this software.

## Features

- **Network Scanning**: Discovers all devices connected to the WiFi network and maps their IP and MAC addresses.
- **Service Discovery**: Identifies open ports and running services on each device.
- **Operating System Detection**: Determines the operating system of connected devices.
- **Vulnerability Assessment**: Checks for common vulnerabilities such as open ports, outdated software, weak passwords, and more.
- **Report Generation**: Creates a comprehensive report detailing the vulnerabilities of each device on the network.
- **Error Handling**: Incorporates robust error handling to ensure reliable scanning and reporting.

## Prerequisites

- Python 3.7+
- Access to the WiFi network you want to scan
- **Permissions** to install and run network scanning tools

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Wifi_Vulnerability_Scanner.git
    cd Wifi_Vulnerability_Scanner
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure your environment:**
    - No additional environment variables are required for this tool.

## Usage

1. **Run the scanner:**
    Go to the root directory of the cloned repository (i.e. Wifi_Vulnerability_Scanner)
    ```bash
    sudo python scripts/run_scan.py
    ```

2. **Monitor the process:**
    - The script will log its progress, including any errors encountered during the scanning process, to the console.

3. **View the report:**
    - The scan report will be generated and saved as `scan_report.txt` in the root directory.

*Note: 

1. With a Small Network (up to 10 devices, /24subnet, standard port scan): Except a 1-5 minute runtime. 

2. With a Method Network (10-50 devices, /24subnet, standard port scan with service detection): Expect a 5-20 minute runtime.

3. With a Large Network (50+ devices, /16 subnet, comprehensive scan including OS detection and service versioning): Expect a 20+ minute to a multiple hours.

## Tips to Optimize Runtime

### Limit the Number of Ports

Scan only the most commonly vulnerable ports (as listed in your README) to reduce the number of checks.

### Adjust Timing Options

Use Nmap timing options (`-T0` to `-T5`) to adjust the aggressiveness of the scan. Higher values are faster but more likely to miss details or cause network disruption.

Example: 
python
nm.scan(hosts=network_range, arguments='-sn -T4')

## Example Output

Your scan report will contain information similar to the following:

P |	MAC |	Status |	Vulnerabilities

192.168.1.2	| 00:1A:2B:3C:4D:5E	up |	Open ssh service on port 22 | product: OpenSSH, version: 7.9
192.168.1.3	| 00:1A:2B:3C:4D:5F	up |	Open http service on port 80 | product: Apache, version: 2.4.41

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-your-feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature-your-feature-name
    ```
5. Open a pull request.

## Commonly Vulnerable Ports

Here are the top 10 most commonly vulnerable ports that the WiFi Vulnerability Scanner will check:

1. **Port 21 (FTP - File Transfer Protocol)**
    - Vulnerabilities: Plaintext transmission of credentials, anonymous authentication, directory traversal attacks.
    - Common Devices: Network-attached storage (NAS), routers, and some IoT devices.

2. **Port 22 (SSH - Secure Shell)**
    - Vulnerabilities: Weak passwords, outdated software, unauthorized access.
    - Common Devices: Linux/Unix servers, network equipment, some IoT devices.

3. **Port 23 (Telnet)**
    - Vulnerabilities: Plaintext transmission of data, weak or no authentication, easily exploitable.
    - Common Devices: Older network equipment, some industrial control systems, IoT devices.

4. **Port 25 (SMTP - Simple Mail Transfer Protocol)**
    - Vulnerabilities: Open relay configurations, email spoofing, unauthorized access.
    - Common Devices: Email servers, multifunction printers.

5. **Port 53 (DNS - Domain Name System)**
    - Vulnerabilities: DNS cache poisoning, DDoS amplification attacks.
    - Common Devices: Routers, DNS servers.

6. **Port 80 (HTTP - Hypertext Transfer Protocol)**
    - Vulnerabilities: SQL injection, cross-site scripting (XSS), weak authentication.
    - Common Devices: Web servers, embedded web interfaces on routers, printers, and IoT devices.

7. **Port 110 (POP3 - Post Office Protocol)**
    - Vulnerabilities: Plaintext transmission of credentials, buffer overflow attacks.
    - Common Devices: Email servers.

8. **Port 143 (IMAP - Internet Message Access Protocol)**
    - Vulnerabilities: Plaintext transmission of credentials, buffer overflow attacks.
    - Common Devices: Email servers.

9. **Port 443 (HTTPS - Hypertext Transfer Protocol Secure)**
    - Vulnerabilities: Misconfigured SSL/TLS settings, outdated encryption protocols.
    - Common Devices: Web servers, embedded web interfaces on devices.

10. **Port 445 (SMB - Server Message Block)**
    - Vulnerabilities: EternalBlue exploit, unauthorized file sharing access.
    - Common Devices: Windows computers, network-attached storage (NAS), printers.

## Acknowledgments

- Special thanks to the open-source community for the libraries and tools used in this project.

## Contact

For any questions or issues, please email me at andrewthielkesoftware@gmail.com.
