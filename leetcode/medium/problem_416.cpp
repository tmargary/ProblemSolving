/*
416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
*/

#include <set>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        set<int> dp;
        dp.insert(0);

        int sum = accumulate(nums.begin(), nums.end(), 0);

        if (sum % 2 != 0)
        {
            return false;
        }

        int target = sum / 2;

        for (int i{}; i < nums.size(); ++i)
        {
            set<int> dp_current;
            for (auto s : dp)
            {
                dp_current.insert(nums[i]);
                dp_current.insert(s + nums[i]);
            }
            if (dp_current.find(target) != dp_current.end())
            {
                return true;
            }
            dp.insert(dp_current.begin(), dp_current.end());
        }

        return (dp.find(target) != dp.end());
    }
};
