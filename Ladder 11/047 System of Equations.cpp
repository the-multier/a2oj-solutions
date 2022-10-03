#include<iostream>
#include<cmath>
using namespace std;
int main() {
    int a,b,c;
    cin>>a>>b;
    c=a+b;
    int d=0;
    for (int i=0;i<=c;i++)
    {
        for(int j=0;j<=c;j++)
        {
            if (((pow(i,2)+(j)==a)&&(pow(j,2)+(i)==b)))
            {
                d=d+1;
            }    
        }
    }
    cout<<d;
 
    return 0;
}