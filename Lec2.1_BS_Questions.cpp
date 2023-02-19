/*
Peak index in a binary array -> Leetcode sum
Example : arr[0]<arr[1]<arr[2]>arr[3]>arr[4] 
*/

# include <iostream>
using namespace std;

int peakIndexInMountainArray(int arr[], int n){
    
    int s = 0;
    int e = n-1;

    int mid = s + (e-s)/2;

    while (s<e){
       if (arr[mid] < arr[mid+1]){
        s = mid + 1;
       } 
       else{
        e = mid;
       }
       mid = s + (e-s)/2;
    }

    return s;
}

int main(){
    int arr[] = {3,4,5,1};
    cout<<peakIndexInMountainArray(arr, 4)<<endl;
}