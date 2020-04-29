"""
1385. Find the Distance Value Between Two Arrays
Easy

61

166

Add to List

Share
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
"""


def findTheDistanceValue(self, arr1, arr2, d):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :type d: int
    :rtype: int
    """
    final_count = 0
    for i in range(len(arr1)):
        count = 0
        for j in range(len(arr2)):
            diff = abs(arr1[i] - arr2[j])
            if diff>d:
                count+=1
        if count == len(arr2):
            final_count+=1
    return final_count