class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

    def fibonacciNumbers(self, count):
        sequence = []
        for i in range(count):
            sequence.append(self.fib(i))
        return sequence



