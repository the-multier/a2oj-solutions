#include <iostream>
using namespace std;
int main()
{
    int a[4];
    int count=0;
    for(int i=0;i<4;i++)
    {
        cin>>a[i];
    }
    for(int j=0;j<4-1;j++)
    {
        for(int k=j+1;k<4;k++)
        if(a[j]==a[k])
        {
            count++;
            break;
        }
    }
    cout<<count;
    return 0;
}
