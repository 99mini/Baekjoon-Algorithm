#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> v;

int main(){
	int n,res=0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		v.push_back(tmp);
	}

	sort(v.begin(), v.end());

	for (int i = 0; i < n; i++) {
		int tmp = 0;
		for (int j = 0; j <= i; j++) {
			tmp += v[j];
		}
		res += tmp;
	}

	cout << res;
}