#include <iostream>
#include <queue>

using namespace std;

queue<int>q;

int dx[3] = { 1,-1 };
int n, k;
int map[100001];
bool check[100001];

int main() {
	cin >> n >> k;

	map[n] = 1;
	check[n] = true;
	q.push(n);

	while (!q.empty()) {
		int curr = q.front();
		dx[2] = curr;
		q.pop();
		for (int i = 0; i < 3; i++) {

			int nx = curr + dx[i];

			if (nx < 100001 && nx >= 0) {
				if (map[nx] == 0 && !check[nx]) {
					
					q.push(nx);
                    map[nx] = map[curr] + 1;
				}
			}
		}
	}

	cout << map[k]-1;
}