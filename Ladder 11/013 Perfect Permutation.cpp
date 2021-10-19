#include <iostream>
using namespace std;
int main() 
{
   int a;
   cin >> a;
   if (a%2==1)
   cout<<"-1";
   else if (a%2==0)
   for(int i=1;i<=a;i=i+2)
   {
       if (a%2==0)
            cout<<i+1<<" "<<i<<" ";
   }
    return 0;
}
