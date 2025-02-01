#include<iostream>
using namespace std;
int main(){
    int num;
    cout<<"\n enter number : ";
    cin>>num;
    int i,count=0;
    for(i=1;i<=num;i++){
        if(num%i==0){
            count++;
        }
    }
    if(count==2){
        cout<<"\n given number "<<num<<" is prime number.";
    }
    else{
        cout<<"\n given number "<<num<<" is not a prime numbar.";
    }
}