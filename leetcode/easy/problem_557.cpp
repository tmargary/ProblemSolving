/*
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.



Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "God Ding"
Output: "doG gniD"

*/

class Solution {
public:
    string reverseWords(string s) {

        int start{};
        int current{};

        while (true){
            // find the next current
            while (s[current] != ' ' && current < s.size()){
                    current++;
                }

            // reverse from start to
            for (int i = start, j=current-1; i < (current + start) / 2; ++i, --j){
                char tmp = s[i];
                s[i] = s[j];
                s[j] = tmp;
            }

            current++;
            start = current;

            if (current > s.size()){
                break;
            }
        }

    return s;

    }
};
