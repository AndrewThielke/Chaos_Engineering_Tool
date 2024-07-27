import unittest
from wifi_scanner.scanner import scan_network

class TestScanner(unittest.TestCase):
    def test_scan_network(self):
        result = scan_network()
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
