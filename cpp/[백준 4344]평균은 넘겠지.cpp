#include <iostream>

using namespace std;

float arr[1001];

int main() {
	
	float c;
	cin >> c;
	for (int i = 0; i < c; i++) {
		int n;
		cin >> n;

		float sum = 0;
		for (int j = 0; j < n; j++) {
			cin >> arr[j];
			sum += arr[j];
		}

		float avg = sum / n;
		float count = 0;

		for (int j = 0; j < n; j++) {
			if (arr[j] > avg) count++;
		}

		printf("%.3f%c\n", ((count * 100 / n) ),'%');
		
	}
}