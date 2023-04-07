/*
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

*/

class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> visited;                            // (n, cnt)
        vector<vector<int>> bucket(nums.size() + 1, vector<int>{}); // (cnt, [nums])

        for (const auto n : nums)
        {
            if (auto search = visited.find(n); search != visited.end())
                ++visited[n];
            else
                visited[n] = 1;
        }

        for (const auto n : visited)
        {
            bucket[n.second].push_back(n.first);
        }

        for (int i{}; i < bucket.size(); ++i)
        {
            cout << i << ": ";
            for (auto n : bucket[i])
            {
                cout << n << " ";
            }
            cout << endl;
        }

        vector<int> res;
        for (int i = bucket.size() - 1; i >= 0; --i)
        {
            for (auto n : bucket[i])
            {
                res.push_back(n);
                if (res.size() == k)
                {
                    return res;
                }
            }
        }

        return res;
    }
};