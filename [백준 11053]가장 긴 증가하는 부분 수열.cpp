#include <iostream>
#define MAX(a,b) a>b ? a:b
using namespace std;

int arr[1001];
int dp[1001];

int main() {
	dp[0] = 1;
	int n,res = 1;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	
	for (int i = 1; i < n; i++) {
		dp[i] = 1;
		for(int j=0;j<i;j++){
			if (arr[i] > arr[j] && dp[i] < dp[j] + 1)
				dp[i] = dp[j] + 1;
		}
		res = MAX(res, dp[i]);
	}
	cout << res;
}