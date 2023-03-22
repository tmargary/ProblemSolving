/*
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

*/

#include <vector>

using namespace std;

class Solution {
public:
    int mark_visited(vector<vector<int>>& grid, int rows, int cols, int r, int c)
    {

        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != 1)
        {
            return 0;
        }

        grid[r][c] = 2;

        int area = 1;
        area += mark_visited(grid, rows, cols, r+1, c);
        area += mark_visited(grid, rows, cols, r-1, c);
        area += mark_visited(grid, rows, cols, r, c+1);
        area += mark_visited(grid, rows, cols, r, c-1);
        return area;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid)
    {
        int max_area = 0;
        int rows = grid.size();
        if (rows == 0)
            return 0;
        int cols = grid[0].size();

        for (int r{}; r<rows; ++r)
        {
            for (int c{}; c<cols; ++c)
            {
                if (grid[r][c] == 1)
                {
                    int area = mark_visited(grid, rows, cols, r, c);
                    max_area = max(max_area, area);
                }
            }
        }
    return max_area;
    }
};
