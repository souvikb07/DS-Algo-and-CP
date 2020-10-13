"""
20. Valid Parentheses
Easy

5824

242

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""

# My solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack=['N']
        m = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in m.keys():
                if stack.pop()!=m[i]:
                    return False
            else:
                stack.append(i)
        return len(stack)==1

# Leet Code Explanation

"""
https://leetcode.com/problems/valid-parentheses/solution/
"""