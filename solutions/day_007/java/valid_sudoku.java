package solutions.day_007.java;

import java.util.HashSet;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        // 1. Create a set to store the numbers
        HashSet<String> hs = new HashSet<>();
        // 2. Check if the number is valid
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                // 3. Add the number to the set
                if (board[i][j] != '.') {
                    String row = "row" + i + board[i][j];
                    String col = "col" + j + board[i][j];
                    int boxnum = ((i / 3) * 3) + (j / 3);
                    String box = "box" + boxnum + board[i][j];
                    if (hs.contains(row) || hs.contains(col) || hs.contains(box))
                        return false;
                    hs.add(row);
                    hs.add(col);
                    hs.add(box);
                }

            }
        }
        return true;
    }

}