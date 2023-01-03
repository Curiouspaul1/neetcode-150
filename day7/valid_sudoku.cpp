#include<iostream>
#include<vector>
#include<map>

using namespace std;

 class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
      map<char,int>boardMap;
    const int size = 9;
    const char dot = '.';

    //check all rows
    for(int row = 0; row < size; ++row){
        for(int col = 0; col < size; ++col){
            if(board[row][col] == dot){
                continue;
            }
            cout << board[row][col] << ' ';
            if(boardMap.count(board[row][col]) == 1){
                return false;
            }
            ++boardMap[board[row][col]];
        }
        boardMap.clear();
        cout << endl;
    }

    cout << endl;
    //check all columns
    for(int col = 0; col < size; ++col){
        for(int row = 0; row < size; ++row){
            if(board[row][col] == dot){
                continue;
            }
            cout << board[row][col] << ' ';
            if(boardMap.count(board[row][col]) == 1){
                return false;
            }
            ++boardMap[board[row][col]];
        }
        boardMap.clear();
        cout << endl;
    }

    cout << endl;
    //check 1st 3X3
    for(int row = 0; row <= 2; ++row){
        for(int col = 0; col <= 2; ++col){
            if(board[row][col] == dot){
                continue;
            }
            cout << board[row][col] << ' ';
            if(boardMap.count(board[row][col]) == 1){
                return false;
            }
            ++boardMap[board[row][col]];
        }
        cout << endl;
    }
        boardMap.clear();

    cout << endl;
    //check 2nd 3X3
    for(int row = 0; row <= 2; ++row){
        for(int col = 3; col <= 5; ++col){
            if(board[row][col] == dot){
                continue;
            }
            cout << board[row][col] << ' ';
            if(boardMap.count(board[row][col]) == 1){
                return false;
            }
            ++boardMap[board[row][col]];
        }
        cout << endl;
    }
        boardMap.clear();

    cout << endl;
    //check 3rd 3x3
    for(int row = 0; row <= 2; ++row){
        for(int col = 6; col <= 8; ++col){
            if(board[row][col] == dot){
                continue;
            }
            cout << board[row][col] << ' ';
            if(boardMap.count(board[row][col]) == 1){
                return false;
            }
            ++boardMap[board[row][col]];
        }
        cout << endl;
    }
        boardMap.clear();

    cout << endl;
    //check 4th 3x3
    for(int row = 3; row <= 5; ++row){
        for(int col = 0; col <= 2; ++col){
            if(board[row][col] == dot){
                continue;
            }
            cout << board[row][col] << ' ';
            if(boardMap.count(board[row][col]) == 1){
                return false;
            }
            ++boardMap[board[row][col]];
        }
        cout << endl;
    }
        boardMap.clear();

    cout << endl;
    //check 5th 3x3
    for(int row = 3; row <= 5; ++row){
        for(int col = 3; col <= 5; ++col){
            if(board[row][col] == dot){
                continue;
            }
            cout << board[row][col] << ' ';
            if(boardMap.count(board[row][col]) == 1){
                return false;
            }
            ++boardMap[board[row][col]];
        }
        cout << endl;
    }
        boardMap.clear();

    cout << endl;
    //check 6th 3x3
    for(int row = 3; row <= 5; ++row){
        for(int col = 6; col <= 8; ++col){
            if(board[row][col] == dot){
                continue;
            }
            cout << board[row][col] << ' ';
            if(boardMap.count(board[row][col]) == 1){
                return false;
            }
            ++boardMap[board[row][col]];
        }
        cout << endl;
    }
        boardMap.clear();

    cout << endl;
    //check 7th 3x3
    for(int row = 6; row <= 8; ++row){
        for(int col = 0; col <=2; ++col){
            if(board[row][col] == dot){
                continue;
            }
            cout << board[row][col] << ' ';
            if(boardMap.count(board[row][col]) == 1){
                return false;
            }
            ++boardMap[board[row][col]];
        }
        cout << endl;
    }
        boardMap.clear();

    cout << endl;
    //check 8th 3x3
    for(int row = 6; row <= 8; ++row){
        for(int col = 3; col <= 5; ++col){
            if(board[row][col] == dot){
                continue;
            }
            cout << board[row][col] << ' ';
            if(boardMap.count(board[row][col]) == 1){
                return false;
            }
            ++boardMap[board[row][col]];
        }
        cout << endl;
    }
        boardMap.clear();

    cout << endl;
    //check 9th 3x3
    for(int row = 6; row <= 8; ++row){
        for(int col = 6; col <= 8; ++col){
            if(board[row][col] == dot){
                continue;
            }
            cout << board[row][col] << ' ';
            if(boardMap.count(board[row][col]) == 1){
                return false;
            }
            ++boardMap[board[row][col]];
        }
        cout << endl;
    }
    boardMap.clear();

    return true;
    }
};