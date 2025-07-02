'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.


'''

# Brute Force Solution, Time Complexity O(n^2), Space Complexity O(n)

class BruteForce:
    def isAnagram(self,s:str,t:str)->bool:
        if len(s)!=len(t):  # Compare the lenght of both strings, if one is longer than the other, the condition if false
            return False
        else:
            t_list=list(t) # Turn the "t" string into a list
            for i in s:   #Iterate over each element of s
                found = False # Create a variable found, for the coincidences between strings if a character in s is found in t
                for j in t_list: #Iterate over each element of the new list of t
                    if i==j:     # Compare between elements of s and t
                        t_list.remove(j) # If there is a coincidence, remove the element from the t list to avoid entering a loop
                        found = True   # Set the found variable to True, as the coincidence has been found
                        break
                if not found:
                        return False #Not found
        
        
        return True
    
#Sorting Solution, Time Complexity O(n log n) due to the sorting method of the strings, Space Complexity O(n)##

class SortedAnagram:
     def isAnagram(self,s:str,t:str)->bool:
          new_s=sorted(s) # Turn the strings into new sorted versions
          new_t=sorted(t)

          if len(new_s) == len(new_t) and new_s == new_t: #Compare if the sorted versions are equal and have the same length
               return True # Valid Anagram
          else:
               return False #Not a valid anagram



#Sorting Solution but optimized, removed redundant condition, Time Complexity O(n log n), Space Complexity O(n)

class SortedAnagramNew:
     def isAnagram(self,s:str,t:str)->bool:
          return sorted(s)==sorted(t)
     
     
# Entry point for running test cases

if __name__ == "__main__":
    solution1 = BruteForce()
    solution2 = SortedAnagram()
    solution3 = SortedAnagramNew()


test_cases = [
        ("racecar", "carrace", True),
        ("jar", "jam", False),
        ("", "", True),
        ("abcd", "abce", False),
        ("aabbcc", "abccba", True),
        ("aabb", "aab", False),
        ("x", "x", True),
        ("x", "y", False),
    ]

for i, (s, t, expected) in enumerate(test_cases):
        result1 = solution1.isAnagram(s, t)
        result2 = solution2.isAnagram(s, t)
        result3 = solution3.isAnagram(s, t)
        print(f"Test Case {i+1}: s='{s}', t='{t}' | Expected: {expected} | Result: {result1} | {'✅' if result1 == expected else '❌'}")
        print(f"Test Case {i+1}: s='{s}', t='{t}' | Expected: {expected} | Result: {result2} | {'✅' if result2 == expected else '❌'}")
        print(f"Test Case {i+1}: s='{s}', t='{t}' | Expected: {expected} | Result: {result3} | {'✅' if result3 == expected else '❌'}")
                                

