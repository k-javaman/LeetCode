class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers
        l, r = 0, len(nums) - 1

        # While the search space is not empty
        while l <= r:
            # Calculate the mid point
            mid = (l + r) // 2

            # If the target is found, return its index
            if target == nums[mid]:
                return mid

            # If the left half is sorted
            if nums[l] <= nums[mid]:
                # If target is greater than mid or smaller than left pointer, it should be in the right half
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # Else it should be in the left half
                else:
                    r = mid - 1
            # If the right half is sorted
            else:
                # If target is less than mid or greater than right pointer, it should be in the left half
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # Else it should be in the right half
                else:
                    l = mid + 1

        # If we reach here, that means the element was not found
        return -1