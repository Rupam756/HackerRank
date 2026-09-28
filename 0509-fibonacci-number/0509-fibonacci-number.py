class Solution:
    def fib(self, n: int) -> int:
        #base csae
        if n == 0 or n == 1:
            return n

        return self.fib(n-1) + self.fib(n-2)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna