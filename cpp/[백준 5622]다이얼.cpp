#include <iostream>
#include <string.h>

using namespace std;

char arr[16];

int dial[26] = { 3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10};

int main() {

	cin >> arr;
	int len = strlen(arr);

	int res = 0;

	for (int i = 0; i < len; i++) {
		res += dial[(int)(arr[i] - 'A')];
	}

	cout << res;
}