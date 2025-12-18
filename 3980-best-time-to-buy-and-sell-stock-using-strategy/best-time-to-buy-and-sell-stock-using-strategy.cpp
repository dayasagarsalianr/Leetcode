#define ll long long
class Solution {
    /***
    Instant thought maybe a sliding window solution would suffice....

    To calculate the initial profit ... we need to just multiply the prices[i]*strategy[i].

    The prices length array is very long so this would require a O(n) or O(nlogn) solution.

    I need suffix sum as well as a prefix sum.

    ss[i]->suffix sum which represents the the profit from day[i] till day[n]
    ps[i]->prefix sum which represents the profilt from day[0] till day[i].
    Then i need to perform a sliding window to calculate the profit from the current window as well
    Solution for a particular window i.....j (i and j included would be)
    ps[i-1]+profit(window)+ss[j+1]

    How do i calculate the profit for the window?
    I know that the window size is even, i can also precalculate the suffix result from window[i+K/2]
    of length k/2 assuming all strategies are 1.


    ***/
public:
    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        ll res=0;
        int n=prices.size();
        vector<pair<ll,ll>>ps(n); //the first stores the actual strategy the second stores values assuming all the strategies are 1.
        vector<pair<ll,ll>>ss(n); //the first stores the actual strategy the second stores values assuming all the strategies are 1.
        ss[n-1].first=prices[n-1]*strategy[n-1];
        ss[n-1].second=prices[n-1];
        res+=prices[0]*strategy[0];
        ps[0].first=res;
        ps[0].second=prices[0];
        for(int i=1;i<n;i++){
            res+=prices[i]*strategy[i];
            ps[i].first=res;
            ps[i].second+=prices[i]+ps[i-1].second;
        }
        for(int i=n-2;i>=0;i--){
            ss[i].first=prices[i]*strategy[i]+ss[i+1].first;
            ss[i].second=prices[i]+ss[i+1].second;
        }

        for(int i=0;i<=n-k;i++){
            //The window starts from i
            ll preRes=(i-1>=0)?ps[i-1].first:0;
            ll suffRes=(i+k<n)?ss[i+k].first:0;
            ll w_r=ps[i+k-1].second-ps[i+k/2-1].second;
            res=max(res,preRes+suffRes+w_r);
        }
        return res;
    }
};