class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) >= k:
            res = heapq.heappop(nums)
        return res
        