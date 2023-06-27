#include <iostream>

using namespace std;

char chess_board[8][8];

int main() {
	int cnt = 0;
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			cin >> chess_board[i][j];
			if ((i + j) % 2 == 0 && chess_board[i][j] == 'F') cnt++;
		}
	}
	cout << cnt;
}