class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify the list nums in-place to produce the next lexicographical permutation.
        """
        n = len(nums)
        
        # Step 1: Find the longest non-increasing suffix
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        # If the entire array is non-increasing, reverse it to the smallest permutation
        if i == 0:
            nums.reverse()
            return
        
        # Step 2: Find the pivot
        pivot = i - 1
        
        # Step 3: Find the rightmost successor to the pivot in the suffix
        j = n - 1
        while nums[j] <= nums[pivot]:
            j -= 1
        
        # Step 4: Swap the pivot with the rightmost successor
        nums[pivot], nums[j] = nums[j], nums[pivot]
        
        # Step 5: Reverse the suffix
        nums[i:] = reversed(nums[i:])
