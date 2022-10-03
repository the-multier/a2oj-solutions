#include <bits/stdc++.h>
using namespace std;
int main() {
    string a,c,d;
    cin>>a;
    int b=a.length();
    for (int i=0;i<b;i++)
    {
        a[i]=tolower(a[i]);
        if (a[i]=='a' || a[i]=='e' ||a[i]=='i' ||a[i]=='o' ||a[i]=='u'||a[i]=='y')
        continue;
        else
        {
        c=a[i];
        d=d+'.'+c;
        }
    }
    cout<<d;
    return 0;
}
