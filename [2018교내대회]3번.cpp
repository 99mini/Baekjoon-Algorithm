#include <iostream>
#include <string>
#include <stack>

using namespace std;

stack<char> s;

int main(){	
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		char str[51];
		cin >> str;

		for (int j = 0; j < strlen(str); j++) {
			if (s.empty()) {
				s.push(str[j]);
			}
			else if (s.top()=='M' && str[j] == 'W') {
				s.pop();
			}
			else {
				s.push(str[j]);
			}
		}
		if (!s.empty()) {
			cout << "no" << endl;
			while (!s.empty()) {
				s.pop();
			}
		}
		else {
			cout << "yes" << endl;
		}
	}

}