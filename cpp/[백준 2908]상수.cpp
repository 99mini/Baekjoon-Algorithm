#include <iostream>

using namespace std;

int a, b;

int main() {

	cin >> a >> b;
	int tmpa = a, tmpb = b;

	for (int i = 0; i < 3; i++) {
		int compa, compb, res = 0;
		compa = tmpa % 10;
		compb = tmpb % 10;

		if(compa > compb) {
			for (int j = 0; j < 3; j++) {
				res *= 10;
				res += a % 10;
				a /= 10;
			}
			cout << res;
			return 0;
		}
		else if (compa < compb) {
			for (int j = 0; j < 3; j++) {
				res *= 10;
				res += b % 10;
				b /= 10;
			}
			cout << res;
			return 0;
		}
		tmpa /= 10;
		tmpb /= 10;
	}
}