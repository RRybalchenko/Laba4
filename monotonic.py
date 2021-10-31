def isMonotonic(nums):
  
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))
  
nums = [1,2,2,3]
  
print(isMonotonic(nums))
