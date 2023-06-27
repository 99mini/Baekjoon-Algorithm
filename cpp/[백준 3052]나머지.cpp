#include <iostream>

using namespace std;

int mod[44];

int main() {
	int cnt = 0;
	for (int i = 0; i < 10; i++) {
		int tmp;
		cin >> tmp;
		mod[tmp % 42]++;
	}

	for (int i = 0; i < 43; i++) {
		if (mod[i]) cnt++;
	}
	cout << cnt;
}