#include <iostream>
#include <string.h>

using namespace std;

int alpa[26];

int main() {
	
	char str[101];
	cin >> str;
	
	int len = strlen(str);

	for (int i = 0; i < len; i++) {
		alpa[str[i] - 'a']++;
	}

	for (int i = 0; i < 26; i++) {
		cout << alpa[i] << ' ';
	}
}