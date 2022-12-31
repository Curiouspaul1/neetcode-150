class Solution {
    public int[] productExceptSelf(int[] nums) {
        // 1. Create an array to store the result
        int answer[] = new int[nums.length];
        // 2. Store the product of all the numbers to the left of the current number
        answer[0] = 1;
        // 3. Store the product of all the numbers to the right of the current number
        for (int i = 1; i < nums.length; i++) {
            // 4. Get the product of all the numbers to the left of the current number
            answer[i] = answer[i - 1] * nums[i - 1];
        }
        // 5. Create a variable to store the product of all the numbers to the right of the current number
        int product = 1;
        // 6. Get the product of all the numbers to the right of the current number
        for (int i = nums.length - 1; i >= 0; i--) {
            // 7. Add the product of all the numbers to the left of the current number and the product of all the numbers to the right of the current number
            answer[i] = answer[i] * product;
            // 8. Get the product of all the numbers to the right of the current number
            product = product * nums[i];
        }
        return answer;
    }
}
