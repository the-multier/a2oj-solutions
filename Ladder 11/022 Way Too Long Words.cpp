#include <iostream>
using namespace std;
int main() 
{
    int a;
    cin>>a;
    for(int i=0;i<a;i++)
    {
        string s;
        cin>>s;
        int l=s.length();
        if(l>10)
        cout<<s[0]<<l-2<<s[l-1]<<endl;
        else
        cout<<s<<endl;
    }
    return 0;
    
}
