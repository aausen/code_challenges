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