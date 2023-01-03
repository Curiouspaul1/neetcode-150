//covert the array to a set
// instantiate the longest variable to be 0
// loop through the array
// if the set contains the current element -1
// then the current element is start of a sequence
// check if the current element + 1 is in the set
// if it is then increment the current element
// and increment the sequence length
// and check again
// if it is not then check if the current element -1 is in the set
// get the maximum of the current sequence length and the longest
// return the longest

import java.util.*;
import java.io.*;

public class d8 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        String[] line = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(line[i]);
        }
        System.out.println(longestConsecutive(arr));
    }

    public static int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int i : nums) {
            set.add(i);
        }
        int longest = 0;
        for (int i : nums) {
            if (!set.contains(i - 1)) {
                int current = i;
                int currentLength = 1;
                while (set.contains(current + 1)) {
                    current++;
                    currentLength++;
                }
                longest = Math.max(longest, currentLength);
            }
        }
        return longest;
    }
}