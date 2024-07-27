import nmap

def get_devices(network_range):
    '''
    Summary Description: This function scans the specified network range for connected devices
                         and retrieves their IP addresses, MAC addresses, and status.

    -- CONTROL FLOW
        -- The function uses the nmap.PortScanner to scan the provided network range.
        -- It iterates through all detected hosts, collecting their IP addresses, MAC addresses, and statuses.
        -- The collected information is stored in a list of dictionaries and returned.

    -- INPUTS
        -- network_range (str): The network range to scan, e.g., "192.168.1.0/24".

    -- OUTPUTS
        -- devices (list): A list of dictionaries containing device information:
            - 'ip' (str): IP address of the device.
            - 'mac' (str): MAC address of the device.
            - 'status' (str): Status of the device (e.g., 'up').

    -- CONSTRAINTS
        -- Requires nmap to be installed on the system.
        -- The user must have the necessary permissions to perform network scans.
    '''
    nm = nmap.PortScanner()
    nm.scan(hosts=network_range, arguments='-sn')
    devices = []
    
    for host in nm.all_hosts():
    
        device = {
            'ip': host,
            'mac': nm[host]['addresses'].get('mac', 'N/A'),
            'status': nm[host].state()
        }
        devices.append(device)
    
    return devices