#include <iostream>
#include <string.h>

using namespace std;

char str[8];
int digit_set[10];

bool check() {
	for (int i = 0; i < 10; i++) {
		if (digit_set[i] > 0) return false;
	}
	return true;
}

int main() {
	
	cin >> str;
	int len = strlen(str);
	int set = 0;
	
	for (int i = 0; i < len; i++) {
		int card = str[i] - '0';
		if (card == 6 || card == 9) {
			if ((digit_set[9] + digit_set[6]) % 2 ) digit_set[9]++;
			else digit_set[6]++;
		}
		else digit_set[card]++;
	}

	while (!check()) {
		for (int i = 0; i < 10; i++) {
			digit_set[i]--;
		}
		set++;
	}
	cout << set;
}