from wifi_scanner.scanner import scan_network

if __name__ == "__main__":
    '''
    Summary Description: This script serves as the entry point for the Wifi_Vulnerability_Scanner. 
                         It imports and invokes the scan_network function to initiate the scanning process.

    -- CONTROL FLOW
        -- The script imports the scan_network function from the wifi_scanner.scanner module.
        -- When executed, it calls the scan_network function to start the network scanning process.

    -- INPUTS
        -- None: The script does not take any command-line arguments or inputs.

    -- OUTPUTS
        -- None: The function logs progress and generates a report file 'scan_report.txt' as part of the scan_network function.

    -- CONSTRAINTS
        -- Requires the wifi_scanner package to be correctly installed and configured.
        -- Assumes that Nmap is installed and accessible on the system.
    '''
    
    scan_network()