class Solution:
    # Define a class Solution which encapsulates the function.

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if (len(nums) == 1):
            return [nums.copy()]

        for i in range(len(nums)):

            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:

                perm.append(n)

            res.extend(perms)

            nums.append(n)

        return res

# Use perms(permutations),res,nums (nums will help to add element ==> more combination
# Start from the whole array and pop each element!