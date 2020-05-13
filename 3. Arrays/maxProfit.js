/**
 * @param {number[]} prices
 * @return {number}
 */
// 122. Best Time to Buy and Sell Stock II
var maxProfit = function(prices) {
    let maxProfit = 0
    for (let idx = 0; idx < prices.length - 1; idx++){
      if (prices[idx] < prices[idx + 1])
        maxProfit+= prices[idx + 1] - prices[idx]
    }

    return maxProfit;
};
