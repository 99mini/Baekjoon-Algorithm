#include <iostream>
#include <string>
#include <string.h>

using namespace std;

char input[1000001];

int main() {

	int count[26] = { 0, };
	
	cin >> input;
	int len = strlen(input);
	for (int i = 0; i < len ; i++) {
		int n;
		if (input[i] >= 'a' && input[i] <= 'z')
			n = input[i] - 'a';
		else
			n = input[i] - 'A';
		
		count[n]++;
	}

	int max = 0;
	int index = -1;

	for (int i = 0; i < 26; i++) {
		if (count[i] >= max) {
			max = count[i];
			index = i;
		}
	}

	for (int i = 0; i < 26; i++) {
		if (count[i] == max && i != index) {
			cout << '?';
			return 0;
		}
	}

	cout << (char)(index + 'A');
}