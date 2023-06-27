#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int n[3];
	cin >> n[0] >> n[1] >> n[2];
	sort(n, n + 3);
	int A, B, C;
	A = n[0];
	B = n[1];
	C = n[2];
	char str[4];
	cin >> str;

	for (int i = 0; i < 3; i++) {
		if (str[i] == 'A') cout << A << ' ';
		if (str[i] == 'B') cout << B << ' ';
		if (str[i] == 'C') cout << C << ' ';
	}

}