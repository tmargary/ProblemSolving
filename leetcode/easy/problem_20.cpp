/*
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
*/

class Solution
{
public:
    bool isValid(string s)
    {

        stack<char> ss;

        std::map<char, char> charMap{
            {'(', ')'},
            {'[', ']'},
            {'{', '}'}};

        for (int i{}; i < s.size(); ++i)
        {
            if (charMap.count(s[i]) == 1)
            {
                ss.push(s[i]);
                continue;
            }

            if (!ss.empty() && s[i] == charMap.at(ss.top()))
            {
                ss.pop();
            }
            else
            {
                return false;
            }
        }

        return ss.empty();
    }
};