// Chap2.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

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