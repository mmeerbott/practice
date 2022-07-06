// Product Except Self
//
// Given an integer array nums, return an array answer such that answer[i]
//  is equal to the product of all the elements of nums except nums[i].
// Must be in O(n) time
//
//
//

function productExceptSelf(nums: number[]): number[] {
  const result = nums.map(n=>1);
  let curProduct = 1;

  for(let i=0; i<nums.length; i++) {
    result[i] = curProduct;
    curProduct *= nums[i];
  }

  curProduct = 1;
  for(let j=nums.length-1; j>=0; j--) {
    result[j] *= curProduct;
    curProduct *= nums[j];
  }

  return result;
};

console.log(productExceptSelf([1,2,3,4]));
// [24,12,8,6]

console.log(productExceptSelf([-1,1,0,-3,3]));
// [0,0,9,0,0]



// Derivation:
// [1,2,3,4]
//  0 1 2 3  <--indices
//i
//0, 1  -  - -
//1, 2  1  - -  c=1, c*=c*n[i-1]
//2, 6  3  2 -
//3, 24 12 8 6  
// notice the current/latest index product is the product of the previous entries
//
// The same works for each index, e.g. [1,2,3]
// 1*2=2 (for index 2)
//
// It can then be repeated backwards to get the products ahead of the index
// numbers (denoted by -)