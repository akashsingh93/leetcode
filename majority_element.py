"""
Submission Detail
46 / 46 test cases passed.
Status: Accepted
Runtime: 160 ms
Memory Usage: 14.9 MB
This algorithm beats 97.85% of pythonic solutions
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict.fromkeys(list(set(nums)),0)
        # counting the numbers 
        print("Before dict ",d)
        for num in nums:
            d[num]+=1
        print("After dict ",d)
        # return max count number
        largest = 0
        ret_key = 0
        for key,value in d.items():
            if largest<value:
                largest = value
                ret_key = key
        return ret_key