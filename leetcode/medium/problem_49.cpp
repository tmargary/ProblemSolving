/*
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

*/

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        unordered_map<string, vector<string>> visited;
        vector<vector<string>> res;

        for (const auto &s : strs)
        {
            string count(26, '0');

            for (auto c : s)
            {
                ++count[c - 'a'];
            }

            visited[count].push_back(s);
        }

        for (auto i : visited)
        {
            res.push_back(move(i.second));
        }
        return res;
    }
};