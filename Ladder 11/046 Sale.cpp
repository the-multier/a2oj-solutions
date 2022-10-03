#include <bits/stdc++.h>
using namespace std;
int main() {
    int a,b;
    cin>>a>>b;
    int arr[a];
    int c;
    for (int i=0;i<a;i++)
    {
        cin>>c;
        arr[i]=c;
    }
    int s=0;
    sort(arr, arr + a);
    for (int j=0;j<b;j++)
    {
        if (arr[j]<0)
        s=s+arr[j];
        else 
        break;
    }
    s=s*(-1);
    cout <<s;
    return 0;
}
