class Solution {
    public int[] twoSum(int[] numbers, int target) {
         int l = 0, r = numbers.length - 1;
    while (numbers[l] + numbers[r] != target) {
        if (numbers[l] + numbers[r] > target) 
            r--;
        else 
            l++;
        if (r == l) return new int[]{};
    }
    return new int[]{l + 1, r + 1};  
    }
}