"""
1313. Decompress Run-Length Encoded List
Easy

130

399

Add to List

Share
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
"""
def decompressRLElist(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sublist = []
    list_len = len(nums)
    if list_len%2==0:
        list_len
    else:
        list_len-=1
    for i in range(0, list_len,2):
        freq = nums[i]
        val = nums[i+1]
        for k in range(freq):
            sublist.append(val)
    return print(sublist)

nums = [1,2,3,4,7]
decompressRLElist(nums)

# Solution 2 
def decompressRLElist(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sublist = []
    for i in range(int(len(nums)/2)):
        freq = nums[2*i]
        val = nums[2*i+1]
        for k in range(freq):
            sublist.append(val)
    return print(sublist)

decompressRLElist(nums)

# solution 3
def decompressRLElist(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    sublist = []
    for i in range(int(len(nums)/2)):
        sublist += [nums[2*i+1]] * nums[2*i]
    return print(sublist)

decompressRLElist(nums)