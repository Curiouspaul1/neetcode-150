import 'dart:collection';

class Solution {
  bool isValidSudoku(List<List<String>> board) {
    // create a hashset to store the numbers in the row, column, and block
    HashSet<String> hashSet = HashSet();
    // loop through the board
    for (int row = 0; row < 9; row++) {
      // loop through the columns
      for (int column = 0; column < 9; column++) {
        // get the number at the current position
        String number = board[row][column];
        // if the number is not a period, add it to the hashset
        if (number != '.') {
          // if the number is already in the hashset, return false
          if (!hashSet.add(number + " in row " + String.fromCharCode(row)) ||
              !hashSet
                  .add(number + " in column " + String.fromCharCode(column)) ||
              !hashSet.add(
                number +
                    " in block " +
                    String.fromCharCode(row ~/ 3) +
                    "," +
                    String.fromCharCode(column ~/ 3),
              )) return false;
        }
      }
    }
    return true;
  }
}
