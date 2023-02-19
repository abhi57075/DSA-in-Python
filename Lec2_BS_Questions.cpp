/*
First and last position of an element in a sorted array

Ex :
2
6 3
0 5 5 6 6 6
8 2
0 0 1 1 2 2 2 2

O/P :
-1 -1
4 7
*/

# include <iostream>
using namespace std;

int firstoccur(int arr[], int n, int key){
    
    int s = 0, e = n-1;
    int mid = s + (e-s)/2;
    int ans = -1;

    while(s<=e){
        
        if (arr[mid]==key){
            ans = mid;
            e = mid-1;
        }
        else if (key > arr[mid]){
            s = mid + 1;
        }
        else if (key < arr[mid]){
            e = mid-1;
        }
        mid = s + (e-s)/2;
    }
    return ans;
}

int lastoccur(int arr[], int n, int key){
    
    int s = 0, e = n-1;
    int mid = s + (e-s)/2;
    int ans = -1;

    while(s<=e){
        
        if (arr[mid]==key){
            ans = mid;
            s = mid + 1;
        }
        else if (key > arr[mid]){
            s = mid + 1;
        }
        else if (key < arr[mid]){
            e = mid-1;
        }
        mid = s + (e-s)/2;
    }
    return ans;
}

int main(){

    int arr[5] = {1,2,3,3,5};
    cout<<firstoccur(arr,5,3)<<endl;
    cout<<lastoccur(arr,5,3)<<endl;

}

/*
Applications : 
Find total number of occurences of 3
Since we know the first occurence of 3 is at index 2
And last occurence of 3 is at index 3
Then 3 has occured (3-2)+1 = 2 times.
*/