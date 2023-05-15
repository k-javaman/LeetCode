class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Two Pointer
        l, r = 0, len(nums) - 1

        while l <= r:
            # # Overflow
            # m = (l + r) // 2
            # No Overflow (Right is always gonna greater than Left)
            m = l + ((r - l) // 2)
            if nums[m] > target: # If the middle value is greater than the target value,
                r = m - 1 # then update the right pointer to be one less than the middle index.
            elif nums[m] < target: # If the middle value is less than the target value,
                l = m + 1 # then update the left pointer to be one more than the middle index.
            else: # If the middle value is equal to the target value,
                return m # then return the index of that value.
        return -1 # If the while loop completes without finding a match, return -1.
