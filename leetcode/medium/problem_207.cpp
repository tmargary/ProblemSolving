/*
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

*/

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:

    bool isCyclic(vector<vector<int>> &adj, vector<int> &visited, int curr)
    {
        if (visited[curr] == processing)
            return true;

        visited[curr] = processing;

        for (int i{}; i < adj[curr].size(); ++i)
            if (visited[adj[curr][i]] != processed)
                if (isCyclic(adj, visited, adj[curr][i]))
                    return true;

        visited[curr] = processed;
        return false;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> visited(numCourses, unvisited);

        for (int i{}; i < prerequisites.size(); ++i)
            adj[prerequisites[i][0]].push_back(prerequisites[i][1]);

        for (int i{}; i < numCourses; ++i)
            if (visited[i] == unvisited)
                if (isCyclic(adj, visited, i))
                    return false;

        return true;
    }

private:
    const int unvisited = 0;
    const int processing = 1;
    const int processed = 2;
};
