#include <bits/stdc++.h>
using namespace std;
int main()
{
    int players;
    int res = 0;
    cin >> players;
    for (int i = 1; i <= players; ++i)
    {
        int prob1, prob2, prob3;
        cin >> prob1 >> prob2 >> prob3;
        if ((prob1 + prob2 + prob3) >= 2)
        {
            res += 1;
        }
    }
    cout << res << endl;
}