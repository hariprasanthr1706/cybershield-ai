import unittest
from detector import analyze_text, analyze_url

class DetectorTests(unittest.TestCase):
    def test_urgent_otp_message_has_signals(self):
        result = analyze_text("Urgent verify now. Send OTP immediately.")
        self.assertTrue(result["signals"])

    def test_neutral_message_has_no_configured_signals(self):
        result = analyze_text("The lecture begins at 10 AM in room 2.")
        self.assertEqual(result["signals"], [])

    def test_http_ip_url_has_signals(self):
        result = analyze_url("http://192.168.1.25/login")
        self.assertTrue(result["signals"])

    def test_example_https_url_has_no_configured_signals(self):
        result = analyze_url("https://example.com")
        self.assertEqual(result["signals"], [])

if __name__ == "__main__":
    unittest.main()
