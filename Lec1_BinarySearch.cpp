/*
Binary search can be applied to only MONOTONIC functions
i.e either strictly increasing or strictly decreasing
*/

# include <iostream>
using namespace std;

int binarySearch (int arr[], int size, int key){
    
    int start = 0;
    int end = size-1;

    int mid = start + (end-start)/2;

    while (start <= end){
        if(arr[mid]==key){
            return mid;
        }
        if(key>arr[mid]){
            start = mid+1;
        }
        else{
            end = mid-1;
        }

        //mid = (start+end)/2;

        /*
        If start = 2^31 -1 and end = 2^31 -1 then mid > range of int
        to handle this smartly we will use : 
        */
       
        mid = start + (end-start)/2;
    }
    return -1;
}

int main(){

    int even[6] = {2,4,6,8,12,18};
    int odd[5] = {3,8,11,14,16};

    int index = binarySearch(even,6,12);

    cout<<index<<endl;
}

/*
Binary Search Time Complexity :

Lets say there are 1000 elements in our array
So reduction of size goes like:
1000->500->250->125->62->31->15->7->3->1->0

Total number of comparisons : 10
Time Complexity : O(logn)

First:  size is N
Second: size is N/2
Third: size is N/4 = N/(2^2)
Fourth: size is N/8 = N/(2^3)
.
.
.
Kth: size is N/(2^k) = 1

therefore : N = 2^k
        : K = logN (log N to the base 2)
*/