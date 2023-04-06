/*
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
*/

#include <string>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        unordered_map<char, int> visited_s;
        unordered_map<char, int> visited_t;

        if (s.size() != t.size())
        {
            return false;
        }

        for (int i{}; i < s.size(); ++i)
        {
            if (auto search = visited_s.find(s[i]); search != visited_s.end())
                ++visited_s[s[i]];
            else
                visited_s[s[i]] = 1;
            if (auto search = visited_t.find(t[i]); search != visited_t.end())
                ++visited_t[t[i]];
            else
                visited_t[t[i]] = 1;
        }

        for (auto i : visited_s)
        {
            if (i.second != visited_t[i.first])
                return false;
        }

        return true;
    }
};
