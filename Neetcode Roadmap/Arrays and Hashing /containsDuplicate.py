'''

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false


'''

from typing import List

#Brute force solution , Time complexity O(n^2), Space Complexity: O(1)

class BruteForce:
    def hasDuplicate(self,nums:List[int])->bool:
        for i in range(len(nums)):  #Iterate over each element of the list
            for j in range (i+1,len(nums)): # Compare with every element ahead of it
                if nums[i] == nums[j]:  # Check for duplication
                    return True
    
        return False  #No duplicates
    

#Sorting solution, Time complexity O(n log n), Space Complexity: O(1)

class SortingList:
    def hasDuplicate(self,nums:List[int])->bool:
        nums.sort()
        for i in range(len(nums)-1): #Iterate over each element of the sorted list
            if nums[i] == nums[i+1]: #Compare an element of the list with the next element of the list to see if they are equal
                return True
        return False # No duplicates
    
#Hashset solution, most optimal solution, Time complexity O(n), Space Complexity: O(n), space complexity in sacrificed due to the possibility of hashset being the same length as the list.

class OptimalSolution:
    def hasDuplicate(self,nums:List[int])->bool:
        hashset = set() # Turn the list into a set

        for n in nums: #Iterate over each element in the list 
            if n in hashset: #Check if the element exist on the list
                return True
            hashset.add(n) #Adds the element if it is not in the set
        return False #No duplicates

        
# Entry point for running test cases
if __name__ == "__main__":
    solution1 = BruteForce()
    solution2 = SortingList()

    # Test cases
    test_cases = [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([99], False),
        ([1, 1, 1, 1], True),
        ([], False),
        ([3, 4, 5, 3, 2, 1], True)
    ]

    # Running and printing results
    for i, (input_list, expected) in enumerate(test_cases):
        result1 = solution1.hasDuplicate(input_list)
        result2 = solution2.hasDuplicate(input_list)
        print(f"Test Case {i + 1}: Input: {input_list} | Expected: {expected} | Result: {result1} | {'✅' if result1 == expected else '❌'}")
        print(f"Test Case {i + 1}: Input: {input_list} | Expected: {expected} | Result: {result2} | {'✅' if result2 == expected else '❌'}")
