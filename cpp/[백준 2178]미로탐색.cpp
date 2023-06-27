#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int maze[101][101];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };

queue<pair<int, int>> q;

void search(int row, int col) {
	q.push(make_pair(0, 0));
	pair<int, int> current;
	int nx, ny;
	while (!q.empty()) {
		current = q.front();
		q.pop();
		for (int i = 0; i < 4; i++) {
			nx = current.second + dx[i];
			ny = current.first + dy[i];

			if (nx >= 0 && nx < col&&ny >= 0 && ny < row&&maze[ny][nx] == 1) {
				q.push(make_pair(ny, nx));
				maze[ny][nx] = maze[current.first][current.second] + 1;
			}
		}
	}

	return;
}

int main() {
	int row, col;
	cin >> row >> col;

	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			scanf("%1d", &maze[i][j]);
		}
	}

	search(row, col);

	cout << maze[row - 1][col - 1];
}