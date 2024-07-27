from setuptools import setup, find_packages

setup(
    name="Wifi_Vulnerability_Scanner",
    version="1.0.0",
    description="Tool that scans and lists vulnerabilities for devices connected to YOUR WiFi network.",
    author="Andrew Thielke",
    author_email="andrewthielkesoftware@gmail.com",
    packages=find_packages(),
    install_requires=[
        "nmap",
        "scapy",
        "prettytable"
    ],
)