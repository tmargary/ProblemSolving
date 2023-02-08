/*
Eliminating duplicates

Your are given an array of size collection_size, containing integers, potentially including duplicates.
An example is

int data[] {1,2,4,5,1,8,2,3,6,1,4,2};

Your job is to write code that eliminates duplicates and print a message exactly like

The collection contains 7 unique numbers, they are : 1 2 4 5 8 3 6

with a single space after the last element, in this case, a space after the 6. Please note that
the message you print has to be exactly formatted like the above one, just adapted for any
collection your code is given as input.  For example,

for an input of int data[] {12,3,21,3,8,2,21,4,3} your code should print The collection contains
6 unique numbers, they are : 12 3 21 8 2 4

for an input of int data[] {7,5,7,2,4,1,7,4,2} your code should print The collection contains 5
unique numbers, they are : 7 5 2 4 1 .

ATTENTION: There should be a single space after the last unique element of the collection you print.
If it's missing, our testing code will flag your program as erroneous!

Your code will go within the comments

       //Don't modify anthing above this line
       //Your code should go below this line

      //Your code should go above this line
      //Don't modify anything below this line


in the exercise.cpp file . Within those two comments, you will have access to an array of int called
numbers, whose size is stored in a variable called collection_size. You are free as you eliminate the
duplicates. The important thing is that for any input array we throw at your code, it produces the
correct output message. Our test code will throw a series of input arrays to your code and check that
we get the correct output message.

You can assume that we will never throw arrays of more than 20 elements to your code.

Please give it your best shot. Once done, you can click on the check solution button to see if you got
it right. If you are still stuck after REALLY trying, you can open the solution.txt file to see our
reference solution to this.
*/

#include <iostream>

void unique_numbers(int numbers[], unsigned int collection_size)
{

    int unique_cnt = 0;
    int num_unique[collection_size] = {};

    for (int i = 0; i < collection_size; ++i)
    {
        int element = numbers[i];
        bool element_exist = false;
        for (int j = 0; j < unique_cnt + 1; ++j)
        {
            if (element == num_unique[j])
            {
                element_exist = true;
                continue;
            }
        }
        if (!element_exist)
        {
            num_unique[unique_cnt] = element;
            unique_cnt++;
        }
    }

    std::cout << "The collection contains " << unique_cnt << " unique numbers, they are : ";

    for (int j = 0; j < unique_cnt; ++j)
    {
        std::cout << num_unique[j] << ' ';
    }
}
