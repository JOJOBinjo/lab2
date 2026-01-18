import unittest
from main import find_domains

class TestDomainRegex(unittest.TestCase):

    def test_valid_domains(self):
        text = "google.com mail.ru example.org"
        self.assertEqual(
            find_domains(text),
            ["google.com", "mail.ru", "example.org"]
        )

    def test_invalid_domains(self):
        text = "google-com -google.com google-.com google@.com"
        self.assertEqual(find_domains(text), [])

    def test_text_domains(self):
        text = "https://github.com https://edu.stankin.ru"
        self.assertEqual(
            find_domains(text),
            ["github.com", "edu.stankin.ru"]
        )

if __name__ == "__main__":
    unittest.main()
