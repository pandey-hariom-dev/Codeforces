#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    int my_row, my_column;
    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= 5; j++)
        {
            cin >> n;
            if (n == 1)
            {
                my_row = i;
                my_column = j;
            }
        }
    }
    cout << abs(3 - my_row) + abs(3 - my_column) << endl;
}