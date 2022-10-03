#include<iostream>
using namespace std;
int main()
{
    int a;
    cin>>a;
    if (a%2==1)
    cout<<-1;
    else
    {
        for(int i=1;i<=a;i+=2)
        {
            cout<<i+1<<" "<<i<<" ";
        }
    }
    return 0;
}
