import logging
from prettytable import PrettyTable

def generate_report(devices):
    '''
    Summary Description: This function generates a comprehensive report of detected devices
                         and their vulnerabilities, and saves it to a text file.

    -- CONTROL FLOW
        -- The function creates a PrettyTable instance to format the report.
        -- It iterates through the list of devices, adding their information and vulnerabilities to the table.
        -- The formatted table is written to a text file named 'scan_report.txt'.

    -- INPUTS
        -- devices (list): A list of dictionaries containing device information and vulnerabilities:
            - 'ip' (str): IP address of the device.
            - 'mac' (str): MAC address of the device.
            - 'status' (str): Status of the device (e.g., 'up').
            - 'vulnerabilities' (list): List of strings describing detected vulnerabilities.

    -- OUTPUTS
        -- None: The function generates a file named 'scan_report.txt' containing the report.

    -- CONSTRAINTS
        -- The function assumes that the devices list is correctly formatted.
        -- The output directory must be writable.
    '''
    table = PrettyTable()
    table.field_names = ["IP", "MAC", "Status", "Vulnerabilities"]
    
    for device in devices:
    
        vulnerabilities = "\n".join(device['vulnerabilities'])
        table.add_row([device['ip'], device['mac'], device['status'], vulnerabilities])
    
    with open("scan_report.txt", "w") as file:
    
        file.write(table.get_string())
    
    logging.info("Scan report generated: scan_report.txt")