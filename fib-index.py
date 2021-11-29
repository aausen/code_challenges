import unittest

# recursive answer
class Fibber(object):

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            raise ValueError('Index was negative. No such thing as a negative index in a series')
        elif n in [0, 1]:
            return n
        if n in self.memo:
            return self.memo[n]
        result = self.fib(n-1) + self.fib(n-2)

        self.memo[n] = result

        return result

# better space/time answer

def fib(n):
    if n < 0:
        raise ValueError('Index was negative. No such thing as a negative index in a series')
    elif n in [0, 1]:
        return n

    prev_prev = 0
    prev = 1

    for _ in range(n-1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current

# The bottom solution is better because it does not use as much time as a simple recursive answer would,
# but it also doesn't use the space that the first example does. The first example uses space
# for the memoization (which is used to help save time). The bottom solution saves both time and space.

class Test(unittest.TestCase):

    def test_zero_fib(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fib(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fib(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_fifth_fib(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fib(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative(self):
        with self.assertRaises(Exception):
            fib(-1)

    
unittest.main(verbosity=2)