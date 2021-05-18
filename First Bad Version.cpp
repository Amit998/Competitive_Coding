#include<iostream>
using namespace std;

class Solution {
    int bad;
public:
    Solution(int bad){
        this->bad = bad;

    }
public:
    bool isBadVersion(int m){
        if (m == bad){
            return true;
        };
        return false;
    }
public:
    int firstBadVersion(int n) {
        int s=1;
        int e=n;
        while(s<e){
            int m= s+(e-s)/2;
            if (isBadVersion(m)){
                e=m;
            }else{
                s=m+1;
            }
        }
        return s;
        
    }
};

int main(){
    int n,bad;

    cin >> n;
    cin>>bad;
    Solution s(bad);
 
    cout<<s.firstBadVersion(n)<<endl;
    return 0;
}
