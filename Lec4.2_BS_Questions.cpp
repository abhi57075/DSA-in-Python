/*
Aggressive cows problem

array = {4,2,1,3,6}
k = 2 (no of cows are 2 c1 and c2)

Distance :
c1 is at 4 and c2 is at 2 = (4-2) = 2
c1 is at 4 and c2 is at 1 = (4-1) = 3
c1 is at 4 and c2 is at 3 = (4-3) = 1
c1 is at 4 and c2 is at 6 = (4-6) = 2
c1 is at 2 and c2 is at 1 = (2-1) = 1
c1 is at 2 and c2 is at 3 = (2-3) = 1
c1 is at 2 and c2 is at 6 = (2-6) = 4
c1 is at 1 and c2 is at 3 = (1-3) = 2
c1 is at 1 and c2 is at 6 = (1-6) = 5
c1 is at 3 and c2 is at 6 = (3-6) = 3

Answer is 5

agar hum ne ek solution nikal liya ki yeh toh pakka nahi hai 
and uske basis pe hum ek particular part ko neglect kar paa rahe hai
then we can apply binary search on the question.

Approach :

min dist = 0
max dist = max - min = 6 - 1 = 5

Search spcae = {0------5}
mid = 2

now try the for loop and from there we see that if 
c1 - c2 >= 2
then store 2 as the ans and s = mid+1
else e = mid-1
*/

# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;

bool isPossible(vector<int> &stalls, int k, int mid){
    int cowCount = 1;
    int lastPos = stalls[0];

    for (int i = 0; i<stalls.size(); i++){
        if (stalls[i]-lastPos >= mid){
            cowCount++;
            if (cowCount == k){
               return true; 
            }
            lastPos = stalls[i];
        }
    }
    return false;
}

int aggressiveCows(vector <int> &stalls, int k){
    
    sort(stalls.begin(), stalls.end());
    int s = 0;
    int maxi = -1;

    for (int i = 0; i<stalls.size(); i++){
       maxi = max(maxi, stalls[i]); 
    }

    int e = maxi;
    int ans = -1;
    int mid = s + (e-s)/2;

    while (s<=e){
        if (isPossible(stalls, k, mid)){
            ans = mid;
            s = mid + 1;
        }
        else{
            e = mid - 1;
        }
        mid = s + (e-s)/2;
    }
    return ans;
}

int main(){
    vector<int> arr = {4,2,1,3,6};
    int k = 2;
    cout<<aggressiveCows(arr,k)<<endl;
}