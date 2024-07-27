import unittest
from wifi_scanner.network_utils import get_devices

class TestNetworkUtils(unittest.TestCase):
    def test_get_devices(self):
        devices = get_devices("192.168.1.0/24")
        self.assertIsInstance(devices, list)

if __name__ == "__main__":
    unittest.main()