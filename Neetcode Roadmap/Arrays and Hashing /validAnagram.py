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
    def validAnagram(self,s:str,t:str)->bool:
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

      
                    

