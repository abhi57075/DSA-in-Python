/*

Selection Sort 

Example : arr[] = {64,25,12,22,11}
    1. arr[] = {11,25,12,22,64}
    2. arr[] = {11,12,25,22,64}
    3. arr[] = {11,12,22,25,64}
    4. arr[] = {11,12,22,25,64}

Total rounds : n-1

Time Complexity : O(n^2)

Space Complexity : O(1) 

Kya maine isko solve karne ke liye koi extra space liya hai?

Humne idhar sirf variables banaye hai aur jab hum variable banate hai sirf,
tab humari space time complexity constant ho jaat hai -> hence O(1).

Best Case : already sorted -> Time Complexity : O(n^2)

Worst Case : sorted in desc order -> Time COmplexity : O(n^2)

Use : When array size is small or when there are memory constraints.
*/

# include <iostream>
using namespace std;

void SelectionSort(int arr[], int n){

    for (int i = 0; i<n-1; i++){
        int minIndex = i;
        for (int j = i+1; j<n; j++){
            if (arr[j] < arr[minIndex]){
                minIndex = j;
            }
        }

        // int temp = arr[i];
        // arr[i] = arr[minIndex];
        // arr[minIndex] = temp;

        swap(arr[minIndex],arr[i]);
    }

}

int main(){

    int arr[] = {64,25,12,22,11};
    SelectionSort(arr, 5);

    for (auto i : arr){
        cout<<i<<" ";
    }
    cout<<endl;
}