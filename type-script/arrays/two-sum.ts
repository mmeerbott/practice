// TwoSum 
// Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
// You may assume that each input would have *exactly one solution*, and you may not use the same element twice.
// You can return the answer in any order.
// NOTE: I am removing the assumption that each input must have a solution, and will return [-1, -1] when there is no solution.
//
// Solution:
// Walk thru the array O(n), subtract the entry from `target` and search. Keep track of the seen number in a hashmap(key: num, value: index_of_entry)
//  so that every entry, the difference can be searched for in O(1), giving the index of the pairing element.
// Time: O(n), n = length of array
// Space: O(2n)

/**
 * Get indices of numbers in nums that add up to target.
 * @param nums    Array of integers to be searched.
 * @param target  The target total that two entries must add up to. 
 * @returns       An array of the two integer indices of the elements that add up to `target`.
 */
function twoSum(nums: number[], target: number): number[] {
  const diffIndices = new Map();
  for (const [i, num] of nums.entries()) {
    const pair = target - num;
    console.log(diffIndices);
    console.log(`see ${num} searching for`, pair);
    if (diffIndices.has(pair)) {
      return [i, diffIndices.get(pair)];
    }
    diffIndices.set(num, i);
  }
  return [-1, -1];
}