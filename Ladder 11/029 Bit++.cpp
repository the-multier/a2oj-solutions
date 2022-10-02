#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int p=0;
    while(t--)
    {
        string x;
        cin>>x;
        if (x.find("++") != string::npos) p++;
        else if (x.find("--") != std::string::npos) p--;
    }
    cout<<p;
    return 0;
}