/*
Hunt for vowels

Given an array of char types, your job is to hunt for vowels in that array and store the
number of vowels in a given variable. For example if you input is

char message[] {'T','h','e',' ','s','k','y',' ' ,'i','s',' ','b','l','u,'e',' ','m',
'y',' ','f','r','i','e,'n','d'};

your code should find that it contains 6 vowels and store the 6 is a specified vowel_count
variable.

Your code will go between the comments

     //Don't modify anything above this line
     //Your code should go below this line


     //Your code should go above this line
     //Don't modify anything below this line

in the exercise.cpp file. You will assume that the characters are stored in an array of
char called message available to you within these two comments.

Once done with the task, you can hit the check solution button and our testing code will
evaluate your code to see if you got this right. Please try and give this your best shot!
If after really trying you are still stuck, you can click on the solution.txt file to see
our reference solution, and learn as much as you can from it

Note : The letter 'y' could either be treated as a vowel or consonant depending on the
letters around it. It's mostly treated as a vowel in fast. However, for simplicity, this
exercise assumes it's a consonant, and that's what our test code will treat it as. As an
exercise, you can write code that treats it as a vowel.
*/

#include <iostream>

void hunt_for_vowels(char message[], unsigned int size)
{

    unsigned int vowel_count{}; // Initialized to zero
    char vowls[] = {'a', 'e', 'i', 'o', 'u'};

    for (int i = 0; i < size; ++i)
    {
        for (int j = 0; j < 5; ++j)
        {
            if (message[i] == vowls[j] || message[i] == toupper(vowls[j]))
            {
                vowel_count++;
                break;
            }
        }
    }

    std::cout << "The string : " << message << " has " << vowel_count << " vowels";
}