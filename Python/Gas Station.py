"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Example
Given 4 gas stations with gas[i]=[1,1,3,1], and the cost[i]=[2,2,1,1]. The starting gas station's index is 2.

Note
The solution is guaranteed to be unique.

Challenge
O(n) time and O(1) extra space
"""

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        """
        if the total number of gas is more than the total cost, there must be a solution.

        """
        gas_sum = min_gas = gas[0] - cost[0]
        result = 0
        for i in range(1, len(gas)):
            gas_sum += gas[i] - cost[i]
            if gas_sum < min_gas:
                min_gas = gas_sum
                result = i
        return (result + 1) % len(gas) if gas_sum >= 0 else -1

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        gas_left = gas_needed = start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            gas_left += g - c
            if gas_left < 0:
                gas_needed -= gas_left
                start = i + 1
                gas_left = 0
        return start if gas_left >= gas_needed else -1
