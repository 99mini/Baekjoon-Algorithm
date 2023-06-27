#include <iostream>
#define MAX(a,b) a > b ? a : b

using namespace std;

int dp[301];
int arr[301];

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	dp[0] = arr[0];
	dp[1] = MAX(arr[0], arr[0] + arr[1]);
	dp[2] = MAX(arr[1] + arr[2], arr[0] + arr[2]);

	for (int i = 3; i < n; i++) {
		dp[i] = MAX(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i]);
	}

	cout << dp[n - 1];
}