#include <stdio.h>

int arr[1001];

int dp(int x) {
	if (x == 1) return 1;
	if (x == 2) return 2;
	if(arr[x]!=0) return arr[x];
	return (arr[x] = dp(x - 2) + dp(x - 1))%10007;
	
}
int main() {

	int num;
	scanf("%d", &num);
	printf("%d", dp(num));

	return 0;
}