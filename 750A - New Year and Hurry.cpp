//109089939	Mar/04/2021 20:31UTC+5.5	Shan_XD	750A - New Year and Hurry	GNU C++17 (64)	Accepted	31 ms	0 KB

    #include<bits/stdc++.h>
    #include<algorithm>
    using namespace std;
    int main()
    {
        int n,k,i,minn=0;
        scanf("%d%d",&n,&k);
        for(i=1;i<=n;i++){
            minn+=i*5;
            if(minn>240-k){
                printf("%d\n",i-1);
                return 0;
            }
        }
        printf("%d\n",i-1);
        return 0;
    }
