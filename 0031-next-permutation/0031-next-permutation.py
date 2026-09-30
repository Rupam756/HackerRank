class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        # Step 2: If we found a valid element, find the next larger element to swap with
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap the two elements
            nums[i], nums[j] = nums[j], nums[i]
            
        # Step 3: Reverse the elements from i + 1 to the end of the array
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna