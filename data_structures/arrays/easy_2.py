"""
1299. Replace Elements with Greatest Element on Right Side
Easy

240

61

Add to List

Share
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        new_arr = []
        for i in range(len(arr)-1):
            new_arr.append(max(arr[i+1:]))
        new_arr.append(-1)
        return new_arr
            
"""
Example : 
[1,21,2,8,7,7,10]
[21,10,10,10,10,-1]

[17,18,5,4,6,1]
[18,6,6,6,1,-1]

Process:
go through every index
check it's right nums
get max number and then 
and append that number in the new list
for last simply add that number in list's last posistion 

O(N)
"""