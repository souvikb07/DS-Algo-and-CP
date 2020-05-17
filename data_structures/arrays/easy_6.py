def checkPossibility(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    length = len(nums)
    if length == 1:
        return True
    count = 0
    for i in range(length - 1):
        if i == 0:
            if nums[i] > nums[i+1]:
                nums[i] = nums[i+1]
                count += 1
        else:
            if nums[i] > nums[i+1]:
                if count == 1:
                    return False
                if nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                count += 1
    return True