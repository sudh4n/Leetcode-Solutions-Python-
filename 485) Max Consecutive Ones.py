"""Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1."""

#Solution

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count1 = count2 = 0
        
        for num in nums:
            if num == 1:
                count2 += 1
                count1 = max(count1, count2)
            else:
                count2 = 0
        return count1
