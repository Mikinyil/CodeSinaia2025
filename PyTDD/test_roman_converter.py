import unittest
from roman_converter import roman_converter

class TestInvalidInput(unittest.TestCase):
    # ======== Step 1 ======== no input, return None
    def test_no_input(self):
        self.assertEqual(roman_converter(None), None)
    def test_str(self):
        self.assertEqual(roman_converter("shaorma"), None)
    def test_dec(self):
        self.assertEqual(roman_converter(3.14), None)
    def test_min(self):
        self.assertEqual(roman_converter(0), None)
    def test_max(self):
        self.assertEqual(roman_converter(4000), "MMMM")
    def test1(self):
        self.assertEqual(roman_converter(1), "I")
    def test2(self):
        self.assertEqual(roman_converter(2), "II")
    def test1000(self):
        self.assertEqual(roman_converter(1000), "M")
    def test1400(self):
        self.assertEqual(roman_converter(1400), "MCD")
    def test4(self):
        self.assertEqual(roman_converter(4), "IV")