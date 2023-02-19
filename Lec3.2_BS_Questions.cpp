/*
We want to remove square root using binary search

Example :
let's say we want to find square root of 27
its sq root will lie between 0---------27.
*/

# include <iostream>
using namespace std;

int sqroot_binarysearch(int n){
    
    int s = 0;
    int e = n;
    long long int mid = s + (e-s)/2;

    long long int ans = -1;

    while (s<=e){
        
        long long int square = mid*mid;

        if (square == n){
            return mid;
        }
        if (square < n){
            ans = mid;
            s = mid+1;
        }
        else{
            e = mid -1;
        }
        mid = s + (e-s)/2;

    }
    return ans;
}

double morePrecision (int n, int precision, int tempsol){

    double factor = 1;
    double ans = tempsol;

    for (int i = 0; i<precision; i++){
        factor = factor/10;
        for (double j = ans; j*j < n; j+=factor){
            ans = j;
        }
    }
    return ans;
}

int main(){
    int x = 27;
    cout<<sqroot_binarysearch(x)<<endl;

    int tempsol = sqroot_binarysearch(x);
    cout<<morePrecision(x,3,tempsol)<<endl;
}