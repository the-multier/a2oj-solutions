#include<iostream>
using namespace std;
int main()
{
int a,b;
cin>>a>>b;
for(int i=a+1;i>0;i++)
{
int count=0;
for(int j=1;j<=i;j++)
{
if(i%j==0)
count++;
}
if(count==2){
if (b==i)
cout<<"YES";
else 
cout<<"NO";
break;
break;
}
}

}
