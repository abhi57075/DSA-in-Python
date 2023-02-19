/*

Bubble Sort

Array : {10,1,7,6,14,9}

Round 1 : arr = {1,10,7,6,14,9}
          arr = {1,7,10,6,14,9}
          arr = {1,7,6,10,14,9}
          arr = {1,7,6,10,14,9}
          arr = {1,7,6,10,9,14}

Round 2 : arr = {1,7,6,10,9,14}
          arr = {1,6,7,10,9,14}
          arr = {1,6,7,10,9,14}
          arr = {1,6,7,9,10,14}

Round 3 : arr = {1,6,7,9,10,14}
          arr = {1,6,7,9,10,14}
          arr = {1,6,7,9,10,14}

Round 4 : arr = {1,6,7,9,10,14}
          arr = {1,6,7,9,10,14}

Round 5 : arr = {1,6,7,9,10,14}

Total number of elements : n
Rounds : n-1

Use : 
After ith round hum ith largest element element ko
array mein uski correct position mein daal dete hai.

Time Complexity : O(n^2) {where n is size of array}

Space Complexity : O(1)

Best Case : already sorted -> O(n)

Optimization :
agar 1st round mein ek bhi swap perform nahi hua hai
toh the array is in sorted order

Worst Case : sorted in desc order -> O(n^2)

*/

# include <iostream>
using namespace std;

void BubbleSort(int arr[], int n){

    for (int i = 1; i<n; i++){
        // for round 1 to n-1
        
        bool swapped = false;

        for (int j = 0; j<n-i; j++){
            // process element till n-i th index

            if (arr[j] > arr[j+1]){
                swap(arr[j],arr[j+1]);
                swapped = true;
            }

        }

        if (swapped == false){
            // already sorted
            break;
        }

    }
}

int main(){

    int arr[] = {10,1,7,6,14,9};
    BubbleSort(arr,6);

    for (auto i : arr){
        cout<<i<<" ";
    }
    cout<<endl;

}