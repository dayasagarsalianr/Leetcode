#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    long long dp[20][11][11][20][2][2];

    long long solve(string &s, int ind, int prev1, int prev2, int waves, int tight, int started)
    {
        int n = s.size();

        if(ind == n)
        {
            if(started == 0) return 0;
            return waves;
        }

        if(dp[ind][prev1+1][prev2+1][waves][tight][started] != -1)
        {
            return dp[ind][prev1+1][prev2+1][waves][tight][started];
        }

        int upper = tight ? (s[ind] - '0') : 9;
        long long ans = 0;
        //  maan lo prevtight ==0 newtight =0 
        //  prevtight==1 and val==upper tight=1;

        for(int d = 0; d <= upper; d++)
        {
            int ntight = (tight && d == upper);

            if(started == 0)
            {
                if(d == 0)
                {
                    ans += solve(s, ind + 1, -1, -1, 0, ntight, 0);
                }
                else
                {
                    ans += solve(s, ind + 1, d, -1, 0, ntight, 1);
                }
            }
            else
            {
                int new_waves = waves;

                if(prev2 != -1)
                {
                    if((prev1 > prev2 && prev1 > d) || (prev1 < prev2 && prev1 < d))
                    {
                        new_waves++;
                    }
                }

                ans += solve(s, ind + 1, d, prev1, new_waves, ntight, 1);
            }
        }

        dp[ind][prev1+1][prev2+1][waves][tight][started] = ans;
        return ans;
    }

    long long totalWaviness(long long L, long long R)
    {
        string s = to_string(L - 1);
        string t = to_string(R);

        memset(dp, -1, sizeof(dp));
        long long left = solve(s, 0, -1, -1, 0, 1, 0);

        memset(dp, -1, sizeof(dp));
        long long right = solve(t, 0, -1, -1, 0, 1, 0);

        return right - left;
    }
};