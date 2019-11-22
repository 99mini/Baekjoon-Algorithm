#include <iostream>
#include <string.h>

using namespace std;

char str[101][101];
int alpa[26];

void reset() {
	for (int i = 0; i < 26; i++) {
		alpa[i] = 0;
	}
}
int main() {
	int n, cnt = 0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> str[i];
	}

	for (int i = 0; i < n; i++) {
		int len = strlen(str[i]);
		bool check = true;
		for (int j = 0; j < len; j++) {
			alpa[str[i][j] - 'a']++;
			if (alpa[str[i][j] - 'a'] > 1 && str[i][j - 1] != str[i][j]) {
				check = false;
				break;
			}
		}
		if (check) cnt++;
		reset();
	}
	cout << cnt;
}