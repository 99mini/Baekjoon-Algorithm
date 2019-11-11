#include <iostream>
#include <queue>

using namespace std;

queue<int> q;

int main() {
	int n, k;
	cin >> n >> k;

	for (int i = 1; i <= n; i++) {
		q.push(i);
	}

	cout << '<';
	while (!q.empty()) {
		for (int i = 1; i < k; i++) {
			int tmp = q.front();
			q.pop();
			q.push(tmp);
		}
		if (q.size() == 1) {
			cout << q.front();
			q.pop();
		}
		else {
			cout << q.front() << ", ";
			q.pop();
		}
	}
	cout << '>';
}