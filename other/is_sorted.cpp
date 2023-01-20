/*
The collection is sorted

Your job is to take in an array of integers and figure out if it is sorted in incremental
order or not.

For example, if we have an input array

int data[] {1,2,4,5,8,12,13,16,71,92};

your code should figure out that the array (collection) is sorted in incrementing order.

If we have an input array

int data[] {1,112,4,5,8,12,13,16,71,92};

your code should figure out that it is not sorted in incrementing order.

You will store your result in a bool variable called sorted. If the collection is sorted,
you'll store in a true, if the collection is not sorted you'll store in a false.

Your code will go between the comments

      // Don't modify anything above this line
      //Your code will go below this line


      //Your code will go above this line
      //Don't modify anything below this line

in the exercise.cpp file.

Within these comments, you have access to the array name numbers and the number of elements
in that array in the variable collection_size.

Once you're done with the exercise, you can hit the check solution button. Our testing code
will throw a bunch of arrays to your code to see if you can if they're sorted or not. Please
give this your best shot. If after REALLY trying you're still stuck, you can click on the
solution.txt file to see our reference solution.
*/


#include <iostream>
#include "exercise.h"

bool is_collection_sorted(int numbers[], unsigned int collection_size){

    bool sorted = true;

    for (int i=0; i<collection_size-2; ++i){
        if (numbers[i] > numbers[i+1]){
            sorted = false;
            break;
        }
    }

  return sorted;
}
