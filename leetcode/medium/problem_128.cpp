/*
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

*/

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        std::set<int> numsSet(nums.begin(), nums.end());
        int res = 0;

        for (auto n : numsSet)
        {
            // check if it's a start of sequance
            if (numsSet.find(n - 1) == numsSet.end())
            {
                int len = 0;
                while (numsSet.find(n + len) != numsSet.end())
                {
                    len++;
                }
                res = max(len, res);
            }
        }
        return res;
    }
};