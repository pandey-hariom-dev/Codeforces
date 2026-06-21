#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    while (n > 0)
    {
        string word;
        cin >> word;
        if (word.length() > 10)
        {
            char last = word.back();
            cout << word[0] << word.length() - 2 << last << endl;
        }
        else
        {
            cout << word << endl;
        }
        n--;
    }
}