/*
Insertion Sort

Array : {1,10,7,4,8,2,11}

Remember sorting cards while playing card games

Total number of rounds : n-1

Use :
It is an adaptable algorithm.
It is a stable algorithm.

Time Complexity : O(n^2)

Space Complexity : O(1)

Best Case : already sorted -> Time Complexity : O(n)
Worst Case : sorted in desc order -> Time Complexity : O(n^2)

*/

# include <iostream>
using namespace std;

void InsertionSort(int arr[], int n){

    for (int i=1; i<n; i++){
        // We assume that the 0th element in the array is sorted

        int temp = arr[i];
        cout<<"The value of temp is : "<<temp<<endl;
        int j = i-1;
        
        for (; j>=0; j--){
            cout<<"The value of arr[j] is : "<<arr[j]<<endl;

            if (arr[j] > temp){
                // shifting towards right
                cout<<"Inside IF condition"<<endl;
                arr[j+1] = arr[j];
            }

            else{
                cout<<"Inside ELSE condition"<<endl;
                break;
            }
        
        } 

        arr[j+1] = temp;

        cout<<endl;

    }
}

int main(){
    //int arr[] = {1,10,7,4,8,2,11};
    
    int arr[] = {10,2,3,1,15};
    InsertionSort(arr,5);

    for (auto i : arr){
        cout<<i<<" ";
    }
    cout<<endl;
}