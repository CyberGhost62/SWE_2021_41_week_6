from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
  # YOUR ANSWER
  result = []
  for i in range (0, len(nums)):
    for j in range (0, len(nums)):
      if(nums[i] + nums[j] == target and i!=j):
        result.append(i)
        result.append(j)
        return result
