E-HCM#include<iostream>
// #include<>
using namespace std;

class Solution{
    double pow_util(double x,long n){
        if (n == 0) return 1.0;
        
        if (n == 1) return x;
      

        if(n < 0) return pow_util(1/x, -n);
       
        
        double result=  pow_util(x*x,n/2);
   

        if (n%2) result *= x;
      
        return result;


    }

    public:
    double myPow(double x,int n){
        return pow_util(x,n);
    };

};

int main(){

    int x=10;
    int n=2;

    Solution sl;
    sl.myPow(x,n );

    return 0;
}
