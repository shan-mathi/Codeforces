//110157726	Mar/17/2021 14:47UTC+5.5	Shan_XD	706B - Interesting drink	GNU C++17 (64)	Accepted	576 ms	400 KB

#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{
    int n,q,i,j,x;
    cin>>n;
    int a[n+10];
    for(i=0;i<n;i++){
        cin>>a[i];
    }
    cin>>q;
    sort(a,a+n);
    for(i=0;i<q;i++){
       cin>>x;
       int ans=upper_bound(a,a+n,x)-a;
       cout<<ans<<endl;
    }
    return 0;
}
