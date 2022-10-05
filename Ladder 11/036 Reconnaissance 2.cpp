#include <iostream>
using namespace std;

#define fo(i, n) for (i = 0; i < n; i++)
#define ll long long
#define pb push_back
#define ppb pop_back
#define ff first
#define ss second
#define nline "\n"
#define el cout << "\n"

int i, n, x, y, minv = 1001;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("Files/Error.txt", "w", stderr);
#endif

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	int arr[n];
	fo(i, n) cin >> arr[i];

	for (i = 0; i < n - 1; i++)
	{
		if (abs(arr[i] - arr[i + 1]) < minv) {
			minv = abs(arr[i] - arr[i + 1]);
			x = i + 1;
			y = i + 2;
		}
	}

	if (abs(arr[0] - arr[n - 1]) < minv) {
		minv = abs(arr[0] - arr[n - 1]);
		x = n;
		y = 1;
	}

	cout << x << " " << y;
	return 0;

}