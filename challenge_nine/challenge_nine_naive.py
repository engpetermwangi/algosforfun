import unittest
from math import inf


def challenge_nine(n):
    n = int(n)
    new_n = inf
    for i in range(9):
        for possible in all_possibles(n, i):
            if possible % 9 == 0:
                new_n = min(new_n, possible)
    return str(new_n)


def all_possibles(n, i):
    n = str(n)
    return (int(n[0:k] + str(i) + n[k:]) for k in range(1 if i == 0 else 0, len(n) + 1))


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
