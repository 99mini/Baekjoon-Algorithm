#include <iostream>
#define MAX(a,b) a>b ? a:b

using namespace std;

int dp[100001];

int main() {
	
	int n, res;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> dp[i];
	}

	res = dp[0];

	for (int i = 1; i < n; i++) {
		if (dp[i - 1] + dp[i] >= dp[i]) 
			dp[i] = dp[i - 1] + dp[i];
		res = MAX(res, dp[i]);
	}
	cout << res;
}