'''
1346. Check If N and Its Double Exist
Easy

124

16

Add to List

Share
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
'''



def checkIfExist(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    final_output = 'false'
    arr.sort(reverse=True)
    print(arr)
    print (len(arr)-1)
    for i in range(len(arr)):
        j=i+1
        print(j)
        while j<len(arr)-1:
            if arr[i] == 2 * arr[j]:
                final_output = 'true'
                print(arr[i],arr[j])
            else:
                None
            j+=1
    return final_output

def checkIfExist(arr):
    s = set(arr)
    print(arr.count(0))
    return arr.count(0) > 1 or any(2 * x in s for x in s if x)

def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        A=arr
        if A.count(0) > 1:
            return True
        S = set(A) - {0}
        for a in A:
            if 2*a in S:
                return True
        return False

print(checkIfExist([3,1,7,11]))