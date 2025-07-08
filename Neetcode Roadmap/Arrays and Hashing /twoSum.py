'''

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000



'''


 

from typing import List

#Brute Force solution  Time Complexity O(n^2)  Space Complexity O(1)

class BruteForce:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        for i in range(len(nums)): #Iterate over each element in the list 
            for j in range(i+1,len(nums)): #Iterate over the list again, with a +1 to the index to avoid self comparisons with the current index  
               if nums[i] + nums[j] == target: # If there are two values in the list that give the target result, return a list with the index of the values
                   return [i,j]
        return []
    


#Sorting solution, not the optimal, not even a bit, test case to proce why this approach does not work. Using two pointers as the solution.  # Time complexity O (n log n) #Space Complexity O(n)

class SortingSolution:
    def twoSum(self, nums:List[int],target:int)->List[int]:
        nums_with_index= [(num,idx) for idx, num in enumerate(nums)] # Creates a new list of tuples, where now the tuple has the value on the list and its index
        nums_with_index.sort() # Sort the new list but keeping the original indexes
        left = 0 # Create a left pointer
        right = len(nums_with_index)-1 # Create a right pointer 
        
        while left < right:
            left_num = nums_with_index[left][0]  
            right_num = nums_with_index[right][0]
            current_sum= left_num + right_num

            if current_sum == target:
                return  [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum< target:
                left += 1
            else:
                right -= 1
            
        return []
    
#Most Optimal Solution : Hashmap impl, Time Complexity O(n) Space Complexity (n) due to the fact that the biggest the hashmap can be is the size of the list

class HashmapSolution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        hashmap = {}    # Create an empty hashmap to store value -> index
        remainder = 0   # Variable to hold the difference between target and current value 
        for i ,num in enumerate(nums):  #Iterate over indices and values in the list
            remainder = target - num    # Calculate the complement needed to reach the target
            if remainder in hashmap:   # If the complement is already in the hashmap
               return [hashmap[remainder],i] # Return indices of the complement and current value
 
            hashmap[num] = i         # Store the current number and its index in the hashmap
        
        return []                      #Return an empty list if there are no matches 

            


    




    # Entry point for running test cases
if __name__ == "__main__":
    solution1 = BruteForce()
    solution2 = SortingSolution()
    solution3 = HashmapSolution()

    # Test cases: each is (input_list, target, expected_output)
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([-3, 4, 3, 90], 0, [0, 2])
    ]

    # Running and printing results
    for i, (nums, target, expected) in enumerate(test_cases):
        result1 = solution1.twoSum(nums, target)
        result2 = solution2.twoSum(nums,target)
        result3 = solution3.twoSum(nums,target)

        is_correct = result1 == expected or result1 == expected[::-1]  # Accept reverse order
        print(f"Test Case {i + 1}: nums={nums}, target={target} | Expected: {expected} | Result: {result1} | {'✅' if is_correct else '❌'}")
        is_correct = result2 == expected or result2 == expected[::-1]  # Accept reverse order
        print(f"Test Case {i + 1}: nums={nums}, target={target} | Expected: {expected} | Result: {result2} | {'✅' if is_correct else '❌'}")
        is_correct = result3 == expected or result3 == expected[::-1]  # Accept reverse order
        print(f"Test Case {i + 1}: nums={nums}, target={target} | Expected: {expected} | Result: {result3} | {'✅' if is_correct else '❌'}")


