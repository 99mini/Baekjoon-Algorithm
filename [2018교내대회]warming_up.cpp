//1시간 소요
#include <iostream>
#include <string>

using namespace std;

class game {
private:
	int out_count;
	int score;
	int inning;
	char base[3];

public:
	game() {
		this->out_count = 0;
		this->inning = 1;
		this->score = 0;
		for (int i = 0; i < 3; i++) {
			base[i] = 'x';
		}
	}

	void init() {
		this->out_count = 0;
		this->inning++;
		for (int i = 0; i < 3; i++) {
			base[i] = 'x';
		}
	}

	void hit(int n) {
		for (int i = 2; i >= 0; i--) {
			if (base[i] == 'o') {
				if (i + n >= 3) this->score++;
				else {
					base[i + n] = 'o';
				}
				base[i] = 'x';
			}
		}
		base[n-1] = 'o';
	}

	void ballNet() {
		for (int i = 2; i >= 0; i--) {
			if (base[i] == 'o') {
				if (i == 2) this->score++;
				else {
					base[i + 1] = 'o';
				}
				base[i] = 'x';
			}
		}
		base[0] = 'o';
	}

	void homeRun() {
		for (int i = 0; i < 3; i++) {
			if (base[i] == 'o') {
				base[i] = 'x';
				this->score++;
			}
		}
	}

	void groundBall() {
		if (this->score == 2) {
			this->out_count++;
			return;
		}
		for (int i = 2; i >= 0; i--) {
			if (base[i] == 'o') {
				if (i == 2) this->score++;
				else {
					base[i + 1] = 'o';
				}
				base[i] = 'x';
			}
		}
		this->out_count++;
	}

	void outFly() {
		if (this->score == 2) {
			this->out_count++;
			return;
		}
		if (base[2] == 'o') {
			base[2] = 'x';
			this->score++;
		}
		this->out_count++;
	}

	//implement K, IF 
	void plusOutCount() {
		this->out_count++;
	}

	void nextInning() {
		if (this->out_count == 3) init();
	}

	int getInning() {
		return this->inning;
	}

	int getScore() {
		return this->score;
	}

	int getOutCount() {
		return this->out_count;
	}

};

int main() {
	int n;
	cin >> n;

	game a, b;

	for (int i = 0; i < n; i++) {
		string input;
		cin >> input;
		
		
		if (a.getInning() - b.getInning()) {
			if (input == "K") b.plusOutCount();
			else if (input == "HR") b.homeRun();
			else if (input == "GO") b.groundBall();
			else if (input == "IF") b.plusOutCount();
			else if (input == "OF") b.outFly();
			else if (input == "BB") b.ballNet();
			else {
				char n = input[0];
				b.hit(n - '0');
			}
		}
		else {
			//a's atack
			if (input == "K") a.plusOutCount();
			else if (input == "HR") a.homeRun();
			else if (input == "GO") a.groundBall();
			else if (input == "IF") a.plusOutCount();
			else if (input == "OF") a.outFly();
			else if (input == "BB") a.ballNet();
			else {
				char n = input[0];
				a.hit(n - '0');
			}
		}
		a.nextInning();
		b.nextInning();
	}

	cout << a.getInning() << '.' << a.getOutCount() << endl;
	cout << a.getScore() << endl;

	cout << b.getInning() << '.' << b.getOutCount() << endl;
	cout <<	b.getScore() << endl;
}