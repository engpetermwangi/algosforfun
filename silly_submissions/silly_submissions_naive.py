import unittest

SPECIAL_KEYS = ["01", "12", "23", "34", "45", "56", "67", "78", "89", "90"]
SPECIALS = {
    "01": "2",
    "12": "3",
    "23": "4",
    "34": "5",
    "45": "6",
    "56": "7",
    "67": "8",
    "78": "9",
    "89": "0",
    "90": "1",
}


def silly_submissions(s):
    prev = None
    while prev != s:
        prev = s
        for special in SPECIAL_KEYS:
            s = s.replace(special, SPECIALS.get(special))
    return s


class TestSillySubmissions(unittest.TestCase):
    def test_sample0(self):
        self.assertEqual(silly_submissions("1"), "1")

    def test_sample1(self):
        self.assertEqual(silly_submissions("012"), "22")

    def test_sample2(self):
        self.assertEqual(silly_submissions("0145"), "26")

    def test_sample3(self):
        self.assertEqual(silly_submissions("00000"), "00000")

    def test_sample4(self):
        self.assertEqual(silly_submissions("98765432101"), "1")


if __name__ == "__main__":
    unittest.main()
