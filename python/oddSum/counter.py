#!/usr/bin/env python3

# Problem:
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# Summary: Return the sum of all odd-length subarrays
#          [1,4,2,5,3] -> [1] [4] ... [1,4,2] [4,2,5] ... [1,4,2,5,3]
#          sum all elements in all those subarrays => 58
#
# Time Analysis:
# generating sub arrays and iterating all of them 
# requires iterating through the original and each sub array (worst
# case length, matching the original array), taking somewhere O(n^2).
# (This is just an estimate, not fully analyzed)
# However, we are only really being asked to look at each element once,
# so the optimal time should be linear O(n)
#
# Strategy:
# It's best to just find out how many times each element would
# be counted and multiply it by that number. Middle numbers should have the 
# highest count. Running through iterations will help find out a pattern.

import math
from typing import List
import time

class OddSum:

    # gets array of the "multipliers"
    # used to help find the linear solution
    # O(n^3) n=length
    def calcOddMultipliers(length: int) -> List[int]:
        arr = [0 for x in range(length)]
        print(f'len:{length}')

        # for odd number within the array's len
        for odd_len in range(1, len(arr)+1, 2):
            # for each idx in array
            for idx in range(len(arr)+1):
                # break when there are too few elements in sub array
                if len(arr) - idx < odd_len:
                    break

                for sub_idx, num in enumerate(arr[idx:]):
                    if sub_idx >= odd_len:
                        break
                    arr[sub_idx+idx] += 1

        return arr


    # creates an array of difference for an array between elements
    # diff[i] = arr[i+1] - arr[i]
    # Used to help find the linear solution by helpig generate the
    # array of multipliers
    # O(n) n=len(arr)
    def printDifferenceBetweenElements(arr: List[int]):
        diff = []
        # for i in range(math.floor(len(arr)/2)):
        for i in range(len(arr)-1):
            diff.append(arr[i+1] - arr[i])

        print(diff)


    # Creates the array of differences required to generate the array
    # of Multipliers
    # The formula was derived on paper thru analyzing the array of diffs
    # O(n) n=length
    def createDifferenceArray(length: int) -> List[int]:
        init_value = math.floor(length/2)-1
        mults = []
        for i in range(length-1):
            if length % 2 == 0:
                mults.append(init_value - i)
            else:
                mults.append(init_value - i + (i%2))
        return mults
    

    # Creates the array of multipliers to multiply an array by
    # to get the sum of odd-length sub arrays
    # O(n) n=length
    def createMultiplierArray(length: int) -> List[int]:
        diffs = OddSum.createDifferenceArray(length)
        mults = [math.ceil(length/2)]

        for i in range(1, length):
            mults.append(mults[i-1] + diffs[i-1])

        return mults

    # Gets the sum of the odd length sub arrays
    # O(n) n=len(arr)
    def sumOfOddLengthSubArrays(arr: List[int]) -> int:
        multipliers = OddSum.createMultiplierArray(len(arr))
        total = 0

        for i, multiplier in enumerate(multipliers):
            total += multiplier * arr[i]

        return total


    # Found online in C++. Calculates multiplier immediately.
    # much less code...
    def simplestSolution(arr: List[int]) -> int:
        res = 0
        length = len(arr)
        for i in range(length):
            start_idx = i + 1
            end_idx = length - i
            multiplier = math.ceil(start_idx * end_idx / 2)
            res += multiplier * arr[i]
        return res
            


if __name__=='__main__':
    array = [1,4,2,5,3,6,8,7,9,11,23,54,3,64,69,42,53,8,99,7,2,4,8,5,8,9,1,52,64,82,96,9,23] 

    start = time.time()
    solution = OddSum.sumOfOddLengthSubArrays(array)
    elapsed = round(time.time() - start, 7)
    print(f'Solution: {solution} ({elapsed} s)')

    start = time.time()
    solution = OddSum.simplestSolution(array)
    elapsed = round(time.time() - start, 7)
    print(f'Simpler Method: {solution} ({elapsed} s)')



