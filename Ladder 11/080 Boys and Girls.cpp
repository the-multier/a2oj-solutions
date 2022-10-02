#include <bits/stdc++.h>
using namespace std;
int main(){
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
    int a,b,c,d;
    string p,q;
    cin>>a>>b;
    c=max(a,b);
    d=min(a,b);
    if (c==d)
    {
        p="G";
        q="B";
    }
    else if(a<b)
    {
        p="G";
        q="B";
    }
    else if(a>b)
    {
        p="B";
        q="G";
    }
    for (int i=1;i<=c;i++)
    {
        if (i<=c)
        cout<<p;
        if (i<=d)
        cout<<q;
    }
    return 0;
}
