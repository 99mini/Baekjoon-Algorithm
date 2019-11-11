#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int nexty[4] = { 1,-1,0,0 };
int nextx[4] = { 0,0,1,-1 };

int field[1001][1001];
int wall;
int res;
int row, col;

queue<pair<int, int>>q;


bool check() {
	int cnt = 0;
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			if (field[i][j] == 1)cnt++;
		}
	}
	return (cnt == row * col - wall);
}

void bfs() {
	if (q.empty()) {
		res = -1;
		return;
	}

	while (!q.empty()) {
		int curr_size = q.size();
		for (int j = 0; j < curr_size; j++) {
			int y = q.front().first;
			int x = q.front().second;

			for (int i = 0; i < 4; i++) {
				int ny = y + nexty[i];
				int nx = x + nextx[i];

				if (ny >= 0 && ny < row && nx >= 0 && nx < col && field[ny][nx] == 0 ) {
					field[ny][nx] = 1;
					q.push(make_pair(ny, nx));
				}
			}

			q.pop();

			if (q.empty()) {
				if(check())
					return;
				else {
					res = -1;
					return;
				}
			}
		}
		res++;
	}
	
}

int main() {
	
	cin >> col >> row;

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			cin >> field[i][j];
			if (field[i][j] == 1) {
				q.push(make_pair(i, j));
			}
			else if (field[i][j] == -1) wall++;
		}
	}

	bfs();

	cout << res;
}