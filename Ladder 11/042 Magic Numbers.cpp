#include <iostream>
#include <string>
using namespace std;
int main() {
    string a;
    cin>>a;
    int b=a.size();
    int c=0;
    for (int i=0;i<b;i++)
    {
        if (a[i]=='1' && a[i+1]=='4' && a[i+2]=='4')
        i=i+2;
        else if (a[i]=='1' && a[i+1]=='4')
        i=i+1;
        else if (a[i]=='1')
        i=i;
        else 
        c=1;
    }
    if (c==0)
    cout<<"YES";
    else 
    cout<<"NO";
    return 0;
}