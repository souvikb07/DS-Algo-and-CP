"""
1331. Rank Transform of an Array
Easy

169

12

Add to List

Share
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
"""


def arrayRankTransform(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    arr_1 = arr[:]
    arr_1.sort()
    list_1 = []
    final_list = []
    j=0
    for i in range(len(arr_1)):
        if i>0 and arr_1[i] != arr_1[i-1]:
            list_1.append(j+1)
        elif i==0:
            list_1.append(j+1)
        elif i>0 and arr_1[i] == arr_1[i-1]:
            list_1.append(j)
            j = j-1
        else:
            list_1.append(j+1)
        j+=1
    dict_1 = dict(zip(arr_1,list_1))
    for j in range(len(arr)):
        final_list.append(dict_1[arr[j]])
    return final_list