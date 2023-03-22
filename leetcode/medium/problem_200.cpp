/*
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
*/

#include <vector>

using namespace std;

class Solution {
public:

    void mark_visited(vector<vector<char>>& grid, int rows, int cols, int r, int c)
    {
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != '1')
        {
            return;
        }

        grid[r][c] = '2';

        mark_visited(grid, rows, cols, r+1, c);
        mark_visited(grid, rows, cols, r-1, c);
        mark_visited(grid, rows, cols, r, c+1);
        mark_visited(grid, rows, cols, r, c-1);
    }

    int numIslands(vector<vector<char>>& grid)
    {
        int cnt = 0;
        int rows = grid.size();
        if (rows == 0)
            return 0;
        int cols = grid[0].size();

        for (int r{}; r<rows; ++r)
        {
            for (int c{}; c<cols; ++c)
            {
                if (grid[r][c] == '1')
                {
                    mark_visited(grid, rows, cols, r, c);
                    cnt++;
                }
            }
        }
    return cnt;
    }
};
