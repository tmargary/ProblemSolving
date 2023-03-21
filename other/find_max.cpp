/*
Where does the big guy live?
You are given an array of integers and your job is to figure out the address where the maximum element in the array lives. For example, given

int data[] {11,2,52,53,9,13,5,7,12,11};
as the input array , you code should figure out that 53 is the maximum and store its address in a variable. Given

int data[] {181,82,22,53,19,1,51,217,12,11};
as the input array, your code should figure out that 217 is the maximum and store its address in a specified variable.

You will put your code between the comments

  //Don't modify anything above this line
  //Your code will go below this line

  //Your code should go above this line
  //Don't modify anything after this line
in the exercise.cpp file. In there you will have access to the array whose name is data , and the size of that array stored in the variable called size. You will also have a  pointer to in variable declared for you named max_address and it is in that variable where  you'll store the address of the maximum element.

Please give this your best shot. If you are still stuck after REALLY trying, you can click on the solution.txt file and take a look at our reference solution.
 */

int*  maximum_address( int data[], unsigned int size){

  int * max_address = &data[0];

  for(unsigned int i=1 ; i < size ; ++i){
    if( data[i] > (*max_address)){
      max_address = &data[i];
    }
  }
  return max_address;
}
