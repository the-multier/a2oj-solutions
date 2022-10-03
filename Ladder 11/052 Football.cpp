#include<bits/stdc++.h>
using namespace std;
int main() {
   string a;
   cin>>a;
   int l=a.size();
   int b=1;
   int arr[l];
   for (int i=0;i<l;i++)
   {
   if (a[i]==a[i+1])
   {
    b=b+1;
    arr[i]=b;
   }
   else if (a[i]!=a[i+1])
  {
   b=0;
    arr[i]=b;
   }
   }
   sort(arr, arr + l);
   b=arr[l-1];
   b=b+1;
   b>=7?cout<<"YES":cout<<"NO";
 
    return 0;
}
