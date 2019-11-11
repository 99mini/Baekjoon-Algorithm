#include <iostream>
#include <string>
#include <queue>

using namespace std;

int map[101][101];

int drow[4] = { 0,0,1,-1 };
int dcol[4] = { 1,-1,0,0 };

int wall;
int sec;
int col, row;

queue<pair<int, int>>q;		//first is row, second is col

bool check() {
	int possible = row * col - wall;
	int cnt=0;
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			if (map[i][j] == 1) cnt++;
		}
	}
	if (possible == cnt) return true;
	else return false;
}

int main() {
	
	cin >> col >> row;

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			cin >> map[i][j];
			if (map[i][j] == 1) q.push(make_pair(i, j));
			else if (map[i][j] == 2) wall++;
		}
	}

	while (!q.empty()) {
		int size = q.size();
		for (int j = 0; j < size; j++) {
			int curr_row = q.front().first;
			int curr_col = q.front().second;

			for (int i = 0; i < 4; i++) {
				int nrow = curr_row + drow[i];
				int ncol = curr_col + dcol[i];

				if (nrow >= 0 && ncol >= 0 && nrow < row && ncol < col && map[nrow][ncol] == 0) {
					map[nrow][ncol] = 1;
					q.push(make_pair(nrow, ncol));
				}
			}
			q.pop();
			if (q.empty() && check()) {
				cout << sec;
				return 0;
			}
			else if (q.empty() && !check()) {
				cout << -1;
				return 0;
			}
		}
		sec++;
	}
}