import unittest


def challenge_nine(n):
    s = sum(map(int, n))
    rem = s % 9
    d = "0" if rem == 0 else str(9 - rem)
    for i, k in enumerate(n):
        if (d == "0" and i > 0) or (d > "0" and k > d):
            return n[0:i] + d + n[i:]
    return n + d


class TestSillySubmissions(unittest.TestCase):
    def test_sample0(self):
        self.assertEqual(challenge_nine("5"), "45")

    def test_sample1(self):
        self.assertEqual(challenge_nine("33"), "333")

    def test_sample2(self):
        self.assertEqual(challenge_nine("12121"), "121212")

    def test_sample3(self):
        self.assertEqual(challenge_nine("32607"), "302607")


if __name__ == "__main__":
    unittest.main()
