#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    int x = 0;
    cin >> n;
    string operation;
    for (int i = 1; i <= n; ++i)
    {
        cin >> operation;
        if (operation[1] == '+')
        {
            x += 1;
        }
        else if (operation[1] == '-')
        {
            x -= 1;
        }
    }
    cout << x << endl;
}