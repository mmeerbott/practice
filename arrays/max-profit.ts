// Max Profit
// You are given an array prices where prices[i] is the price of a given stock on the ith day.
// You want to maximize your profit by choosing a single day to buy one stock and choosing a 
//   different day in the future to sell that stock.
// Return the maximum profit you can achieve from this transaction. If you cannot achieve any
//   profit, return 0.
// 
// Solution:
// Start from beginning, slide a window through the array testing min/max values
// Time: O(n)
// space: O(n)

function maxProfit(prices: number[]): number {
  let minIndex = 0;
  let maxIndex = 1;
  let diff = prices[maxIndex] - prices[minIndex];
  let maxProfit = 0;
  
  while (maxIndex < prices.length) {
    if (prices[minIndex] < prices[maxIndex]) {
      diff = prices[maxIndex] - prices[minIndex];
      maxProfit = diff > maxProfit ? diff : maxProfit; 
    }
    else {
      minIndex = maxIndex;
    }
    maxIndex += 1;
  }
  return maxProfit;
};

console.log('4 ==', maxProfit([3,2,6,5,0,3]));
console.log('1 ==', maxProfit([2,1,2,1,0,0,1]));
