class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #check gcd 
        if str1 + str2 != str2 + str1:
            return ""

        import math

        length = math.gcd(len(str1),len(str2))

        return str1[:length]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna