class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            return 1.0 / self.myPow(x, -n)

        half = self.myPow(x, n//2) 

        if n%2 == 0:
            return half*half
        else:
            return half * half * x
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna