#include <iostream>
#include <vector>

using namespace std;

pair<int, int> start, arrive;
int circle[3][51];

int length(int x1, int y1, int x2, int y2){
	return (int)sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int result = 0;
		cin >> start.first >> start.second >> arrive.first >> arrive.second;
		
		int n;
		cin >> n;

		for (int j = 0; j < n; j++) {
			cin >> circle[0][j] >> circle[1][j] >> circle[2][j];
		}
		for (int j = 0; j < n; j++) {
			if (length(start.first, start.second, circle[0][j], circle[1][j]) < circle[2][j]) result++;
			else if (length(arrive.first, arrive.second, circle[0][j], circle[1][j]) < circle[2][j]) result++;

			if (length(start.first, start.second, circle[0][j], circle[1][j]) < circle[2][j]
				&& length(arrive.first, arrive.second, circle[0][j], circle[1][j]) < circle[2][j])
				result--;
		}
		cout << result << endl;
	}
}