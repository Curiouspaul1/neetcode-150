 /**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
  let validSq = (num, posRow, posCol) => {
    let startCol = posCol - posCol % 3; 
    let startRow = posRow - posRow % 3;
      for (let row = startRow; row < startRow + 3; row ++){
        for (let col = startCol; col < startCol + 3; col ++){
          if (row != posRow && col != posCol && board[row][col] === num) return false;
        }
      }
    return true;
  }
  
  let validRow = (num, row, posCol) => {
    for (let col = 0; col < board[0].length; col++){
      if (col !== posCol && board[row][col] === num) return false;
    }
    return true;
  }
  
  let validCol = (num, posRow, col) => {
    for (let row = 0; row < board.length; row++){
      if (row !== posRow && board[row][col] === num) return false;
    }
    return true;
  }
  
  for (let row = 0; row < board.length; row++){
    for (let col = 0; col < board[0].length; col++){
      if (board[row][col] !== '.'){
        let args = [board[row][col], row, col];
        if ([validSq, validRow, validCol].some(f => !f(...args))) return false
      }
    }
  }
  return true;
};