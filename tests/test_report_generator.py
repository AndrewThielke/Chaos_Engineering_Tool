import unittest
from wifi_scanner.report_generator import generate_report

class TestReportGenerator(unittest.TestCase):
    def test_generate_report(self):
        devices = [{
            'ip': '127.0.0.1',
            'mac': '00:00:00:00:00:00',
            'status': 'up',
            'vulnerabilities': ['Sample vulnerability']
        }]
        generate_report(devices)
        with open("scan_report.txt", "r") as file:
            content = file.read()
            self.assertIn("127.0.0.1", content)

if __name__ == "__main__":
    unittest.main()