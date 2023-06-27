#include <iostream>

using namespace std;

int house[1001][3];
int dp[1001][3];

int min(int a, int b) {
	return a < b ? a : b;
}

int main() {
	int num;
	cin >> num;

	for (int i = 1; i <= num; i++) {
		for (int j = 0; j < 3; j++)
			cin >> house[i][j];
	}

	for (int i = 1; i <= num; i++) {
		dp[i][0] = house[i][0] + min(dp[i - 1][1], dp[i - 1][2]);
		dp[i][1] = house[i][1] + min(dp[i - 1][0], dp[i - 1][2]);
		dp[i][2] = house[i][2] + min(dp[i - 1][0], dp[i - 1][1]);
	}

	cout << min(min(dp[num][0], dp[num][1]), dp[num][2]);
}