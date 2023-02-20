/*
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
*/

class Solution
{
public:
    std::stack<char> getPost(const string &s)
    {
        char del = '#';
        std::stack<char> ss;

        for (int i{}; i < s.size(); ++i)
        {
            if (s[i] == del)
            {
                if (!ss.empty())
                    ss.pop();
            }
            else
            {
                ss.push(s[i]);
            }
        }
        return ss;
    }

    std::string stackToString(std::stack<char> &charStack)
    {
        std::string str;
        while (!charStack.empty())
        {
            str += charStack.top();
            charStack.pop();
        }

        return str;
    }

    bool backspaceCompare(string s, string t)
    {

        std::stack<char> ss = getPost(s);
        std::stack<char> tt = getPost(t);

        if (ss.size() != tt.size())
            return false;

        if (stackToString(ss) == stackToString(tt))
            return true;
        return false;
    }
};