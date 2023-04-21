class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}                  # create a dictionary to count the frequency                                        of each number
        freq = [[] for i in range(len(nums) + 1)]   # create a list of lists to                                     store the numbers grouped by frequency

        for n in nums:              # iterate through the input numbers
            count[n] = 1 + count.get(n, 0)   # count the frequency of each number                                               in the dictionary
                                    # count[n] -> the key of the dictionary

        for n,c in count.items():   # iterate through the dictionary
            freq[c].append(n)       # group the numbers by frequency in the list                                    of lists

        res = []                    # create an empty list to store the final                                       result
        for i in range(len(freq) - 1, 0, -1):   # iterate through the list of                                       lists in reverse order
            for n in freq[i]:       # iterate through the list of numbers with                                      the same frequency
                res.append(n)       # add the number to the final result list
                if(len(res) == k):  # if we have added k numbers to the result                                      list, we're done
                    return res

        return res                  # return the final result list