// Chap5_HW_Saving.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
#include "SavingsAccount.h"
using namespace std;

int main()
{
    // std::cout << "Hello World!\n";
    Date date(2018, 11, 1);
    SavingsAccount accounts[] = {
        SavingsAccount(date, "S123456", 0.015),
        SavingsAccount(date, "L005311", 0.015)
    };
    accounts[0].deposit(Date(2018, 11, 5), 5000, "salary");
    accounts[1].deposit(Date(2018, 11, 25), 10000, "sell stock");

    accounts[0].deposit(Date(2018, 12, 5), 5500, "salary");
    accounts[1].withdraw(Date(2018, 12, 20), 4000, "buy a girlfriend.");

    cout << endl;

    const int n = sizeof(accounts) / sizeof(SavingsAccount);
    for (int i = 0; i < n; i++) {
        accounts[i].settle(Date(2019, 1, 1));
        accounts[i].show();
        cout << endl;
    }
    cout << "Total:" << SavingsAccount::getTotal() << endl;

    return 0;
}