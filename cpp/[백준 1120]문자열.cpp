#include <iostream>
#include <string.h>

using namespace std;

int main(){
    
	char n[51], m[51];
	cin >> n >> m;

	int diff = strlen(m) - strlen(n);
	int min = 51;
	
	for (int i = 0; i <= diff; i++) {
		int tmp = 0;
		for (int j = 0; j < strlen(n); j++) {
			if (n[j] != m[j+i]) tmp++;
		}
		if (min > tmp) min = tmp;
	}

	cout << min;
}
