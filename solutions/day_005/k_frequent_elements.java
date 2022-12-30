import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // 1. Count the frequency of each number
        Map<Integer,Integer> numToFreq = new HashMap<>();
        // 2. Sort the numbers by frequency
        for(int num : nums) {
            // 3. Get the top k numbers
            int occurance = numToFreq.getOrDefault(num, 0);
            // 4. Add the numbers to the result
            numToFreq.put(num, occurance + 1);
        }
        // 5. Return the result
        TreeMap<Integer, List<Integer>> freqToNumbers = new TreeMap<>();
        // 6. Sort the numbers by frequency

        for(int key : numToFreq.keySet()) {
            // 7. Get the top k numbers
            freqToNumbers.putIfAbsent(numToFreq.get(key), new ArrayList<Integer>());
            // 8. Add the numbers to the result
            freqToNumbers.get(numToFreq.get(key)).add(key);
            // 9. Return the result
        }
        int[] res = new int[k];
        int index = 0;
        for(int i = 0; i < k; i++) {
            // 10. Get the top k numbers
            Map.Entry<Integer,List<Integer>> lastEntry = freqToNumbers.lastEntry();
            // 11. Add the numbers to the result
            List<Integer> values = lastEntry.getValue();
            res[index++] = values.remove(0);
            if(values.size() == 0)
                freqToNumbers.remove(lastEntry.getKey());
        }
        return res;
    }
}