# include <iostream>
using namespace std;

int main() {
	int n, sum = 0, base, mod;
	cin >> n;
	base = 1;
	do {
		mod = n % 10;
		sum += mod * base;
		base *= 2;
		n = n / 10;
	} while (n > 0);
	cout << sum;
	return 0;
}