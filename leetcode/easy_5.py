"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# solution 1
def fib(n):
    output = [1,2]
    if 1<=n<=2:
        return output[n-1]
    else:
        if fib(n-1) + fib(n-2) not in output:
            output.append(fib(n-1) + fib(n-2))
            return fib(n-1) + fib(n-2)
print(fib(19))

# solution 2

class Solution:
    def climbStairs(self, n: int) -> int:
        current = previous = 1
        for _ in range(n-1):
            current, previous = current + previous, current
        return current
            