import nmap
import logging

def get_devices(network_range):
    '''
    Summary Description: This function scans the specified network range for connected devices
                         and retrieves their IP addresses, MAC addresses, status, and operating systems.

    -- CONTROL FLOW
        -- The function uses the nmap.PortScanner to scan the provided network range.
        -- It iterates through all detected hosts, collecting their IP addresses, MAC addresses, statuses, and OS information.
        -- The collected information is stored in a list of dictionaries and returned.

    -- INPUTS
        -- network_range (str): The network range to scan, e.g., "192.168.0.0/24".

    -- OUTPUTS
        -- devices (list): A list of dictionaries containing device information:
            - 'ip' (str): IP address of the device.
            - 'mac' (str): MAC address of the device.
            - 'status' (str): Status of the device (e.g., 'up').
            - 'os' (str): Operating system of the device.

    -- CONSTRAINTS
        -- Requires nmap to be installed on the system.
        -- The user must have the necessary permissions to perform network scans.
    '''
    logging.info(f"Scanning network range {network_range} for devices...")
    nm = nmap.PortScanner()
    try:
        # Use -A for comprehensive scan including OS detection and service version detection
        nm.scan(hosts=network_range, arguments='-A -p 21,22,23,25,53,80,110,143,443,445')
        devices = []
        
        for host in nm.all_hosts():
            logging.info(f"Host found: {host}")
            device = {
                'ip': host,
                'mac': nm[host]['addresses'].get('mac', 'N/A'),
                'status': nm[host].state(),
                'os': "Unknown",
                'os_details': "Unknown"
            }
            
            if 'osclass' in nm[host] and len(nm[host]['osclass']) > 0:
                os_class = nm[host]['osclass'][0]
                device['os'] = f"{os_class['osfamily']} {os_class['osgen']}"
                device['os_details'] = os_class.get('accuracy', 'Unknown')
            
            elif 'osmatch' in nm[host] and len(nm[host]['osmatch']) > 0:
                os_match = nm[host]['osmatch'][0]
                device['os'] = os_match['name']
                device['os_details'] = os_match.get('accuracy', 'Unknown')
            
            else:
                logging.info(f"No OS information available for {host}")
            
            devices.append(device)
        
        logging.info(f"Network scan completed. {len(devices)} devices found.")
        return devices
    
    except Exception as e:
        logging.error(f"Error during network scan: {e}")
        return []