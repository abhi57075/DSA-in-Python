/*
Find pivot in an array

array : {1,2,3,7,9}
rotated array : {7,9,1,2,3} -> input

Here 1 is the pivot element
*/

# include <iostream>
using namespace std;

int getPivot(int arr[], int n){
    
    int s = 0;
    int e = n-1;
    int mid = s + (e-s)/2;

    while(s<e){
        if (arr[mid]>=arr[0]){
            s = mid + 1;   
        }
        else{
            e = mid;
        }
        mid = s + (e-s)/2;
    } 
    return s; // or return e
}

int main(){
    int arr[5] = {8,10,17,1,3};
    cout<<getPivot(arr,5)<<endl;
}

/*
Let us take the array {3,8,10,17,1} s = 0, e = 4

arr[mid] = arr[2] = 10
arr[mid] >= arr[0] True s = 3, e = 4

arr[mid] = arr[3] = 17
arr[mid] >= arr[0] True s = 4, e = 4

Here s<e is false hence return e which is 4

arr[mid] = arr[4] = 1
arr[mid] >= arr[0] False s = 4, e = 4
*/