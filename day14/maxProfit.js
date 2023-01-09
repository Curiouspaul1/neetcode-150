/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = (prices) => {
  let l = 0, r = 1;
  let max = 0;
  while (r < prices.length) {
    if (prices[l] < prices[r]) {
      let temp = prices[r] - prices[l];
      max = Math.max(max, temp);
    } else { l = r; }
    r++;
  }
  return max;
};
