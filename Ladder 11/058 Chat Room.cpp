#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main() {
    string a;
    cin>>a;
    int b=a.size();
    int c=0;
    for (int i=0;i<b;i++)
    {
        if (a[i]=='h')
        {
            c=i;
            break;
        }    
    }
    int d=0;
    for (int i=c+1;i<b;i++)
    {
        if (a[i]=='e')
        {
            d=i;
            break;
        }
    }
    int e=0;
    for (int i=d+1;i<b;i++)
    {
        if (a[i]=='l')
        {
            e=i;
            break;
        }
    }
    int f=0;
    for (int i=e+1;i<b;i++)
    {
        if (a[i]=='l')
        {
            f=i;
            break;
        }
    }
    int g=0;
    for (int i=f+1;i<b;i++)
    {
        if (a[i]=='o')
        {
            g=i;
            break;
        }
    }
    if ((0<=c)&&(c<d)&&(d<e)&&(e<f)&&(f<g))
    cout<<"YES";
    else 
    cout<<"NO";
    
    return 0;
}