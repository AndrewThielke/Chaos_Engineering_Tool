# Wifi_Vulnerability_Scanner

## Overview

The **Wifi_Vulnerability_Scanner** is a Python-based tool designed to scan and list vulnerabilities for devices connected to a WiFi network. This tool identifies devices, detects open ports and services, assesses operating systems, and checks for known vulnerabilities. It provides a comprehensive report to help network administrators and security enthusiasts ensure the security and resilience of their networks.

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
- Permissions to install and run network scanning tools

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
    ```bash
    python scripts/run_scan.py
    ```

2. **Monitor the process:**
    - The script will log its progress, including any errors encountered during the scanning process, to the console.

3. **View the report:**
    - The scan report will be generated and saved as `scan_report.txt` in the root directory.

## Example Output

Your scan report will contain information similar to the following:

P |	MAC |	Status |	Vulnerabilities
192.168.1.2	| 00:1A:2B:3C:4D:5E	up |	Open ssh service on port 22 | product: OpenSSH, version: 7.9
192.168.1.3	| 00:1A:2B:3C:4D:5F	up |	Open http service on port 80 | product: Apache, version: 2.4.41

## Project Structure

Wifi_Vulnerability_Scanner/
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── .gitignore
├── wifi_scanner/
│ ├── init.py
│ ├── scanner.py
│ ├── network_utils.py
│ ├── vulnerability_checks.py
│ ├── report_generator.py
│ └── config.py
├── tests/
│ ├── init.py
│ ├── test_scanner.py
│ ├── test_network_utils.py
│ ├── test_vulnerability_checks.py
│ └── test_report_generator.py
└── scripts/
└── run_scan.py


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

## Acknowledgments

- Special thanks to the open-source community for the libraries and tools used in this project.

## Contact

For any questions or issues, please email me at andrewthielkesoftware@gmail.com.
