import logging
from .config import LOG_LEVEL, NETWORK_RANGE, SCAN_PORTS
from .network_utils import get_devices
from .vulnerability_checks import check_vulnerabilities
from .report_generator import generate_report

logging.basicConfig(level=LOG_LEVEL)

def scan_network():
    '''
    Summary Description: This function orchestrates the network scanning process, including device discovery,
                         vulnerability assessment, and report generation.

    -- CONTROL FLOW
        -- The function initiates a network scan to discover connected devices using get_devices.
        -- For each discovered device, it checks for vulnerabilities using check_vulnerabilities.
        -- It collects the scan results and generates a report using generate_report.

    -- INPUTS
        -- None

    -- OUTPUTS
        -- None: The function logs progress and generates a report file 'scan_report.txt'.

    -- CONSTRAINTS
        -- Requires network access and necessary permissions to perform scans.
        -- Assumes that the configuration settings in config.py are correctly set.
    '''
    logging.info("Starting network scan...")
    devices = get_devices(NETWORK_RANGE)
    logging.info(f"Found {len(devices)} devices.")
    
    for device in devices:
        
        logging.info(f"Scanning device {device['ip']}...")
        vulnerabilities = check_vulnerabilities(device['ip'])
        device['vulnerabilities'] = vulnerabilities
    
    generate_report(devices)

if __name__ == "__main__":
    
    scan_network()