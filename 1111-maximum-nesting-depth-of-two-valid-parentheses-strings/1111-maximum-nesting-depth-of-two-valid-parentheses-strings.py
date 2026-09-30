class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        d = 0
        res = []

        for c in seq:
            if c == '(':
                res.append(d%2)
                d += 1
            else:
                d -= 1
                res.append(d % 2)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna