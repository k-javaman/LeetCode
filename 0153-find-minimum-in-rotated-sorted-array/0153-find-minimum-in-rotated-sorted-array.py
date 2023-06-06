class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # find if the array is sorted, if it's sorted, break and return the res
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break

            m = (l + r) // 2
            
            res = min(res, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
