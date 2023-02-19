/*
Book Allocation Problem

Array of Books : {10,20,30,40}
The elements in the array represent s the pages

Conditions : 
1. Each student gets at least one book
2. Each book should be allocated to a student
3. Book allocation should be in a contiguous manner.
i.e if 2 students are there then we can allocate them books with {10,20,30} pages and other one with {40} pages
but not like {10,30} and {20,40}

We have to allocate the book to m students such that the maximum number of pages assigned to a student is minimum


Example  n = 4 and m = 2
array : {10,20,30,40}

Possible ways :
1. {10}{20,30,40} = max(10,90) = 90 
2. {10,20}{30,40} = max(30,70) = 70  
3. {10,20,30}{40} = max(60,40) = 60

min (90,70,60) = 60

Answer is 60

Approach:

answer's search space will be from 0 to (10+20+30+40)100
0-----------100

mid = 50
we will check if 50 is a possible solution or not?

here m = 2

s1 = 10,20 {since 10 + 20 <= 50}
s2 = 30 
now one book is remaining and all the students have received the book
hence 50 is not a possible solution

hence s = mid + 1

now our search space becomes from {51----100}
apply the same process again

*/

# include <iostream>
# include <vector>
using namespace std;

bool isPossible(vector<int>arr, int n, int m, int mid){
    int studentCount = 1;
    int pageSum = 0;

    for (int i = 0; i<n; i++){
        if (pageSum + arr[i] <= mid){
            pageSum += arr[i];
        }
        else{
            studentCount++;
            if (studentCount > m || arr[i] > mid){
                return false;
            }
            pageSum = 0;
            pageSum += arr[i];
        }
    }
    return true;
}

int allocateBooks (vector<int> arr, int n, int m){
    int s = 0;
    
    int sum = 0;
    for (int i = 0; i<n; i++){
        sum += arr[i];
    }

    int e = sum;
    int mid = s+(e-s)/2;
    int ans = -1;

    while (s<=e){
        if (isPossible(arr,n,m,mid)){
            ans = mid;
            e = mid-1;
        }
        else{
            s = mid + 1;
        }
        mid = s + (e-s)/2;
    }
    return ans;
}

int main(){
    vector <int> arr = {10,20,30,40};
    int m = 2;
    cout<<allocateBooks(arr,4,2)<<endl;
}