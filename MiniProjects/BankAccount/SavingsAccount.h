#ifndef SAVINGSACCOUNT_H_
#define SAVINGSACCOUNT_H_
#include "Date.h"
#include <string>

#pragma once
class SavingsAccount
{ // 邮储账户类
private:
	std::string id; // 账号
	double balance; // 余额
	double rate; // 存款年利率
	Date lastDate; // 上次变更余额的日期
	double accumulation; // 余额按日累加之和
	static double total; // 所有账户的总金额
	// 记录一笔账，date为日期， amount为金额  
	void record(const Date &date, double amount, const std::string &desc);
	void error(const std::string& msg) const;
	double accumulate(Date date) const {
		return accumulation + balance * date.distance(lastDate);
	}

public:
	// 构造函数
	SavingsAccount(const Date &date, const std::string &id, double rate);
	const std::string getId() const { return id; }
	double getBalance() const { return balance; }
	double getRate()const { return rate; }
	static double getTotal() { return total;}

	// 存入现金
	void deposit(const Date &date, double amount, const std::string &desc);
	// 取出现金
	void withdraw(const Date &date, double amount, const std::string &desc);
	// 结算利息
	void settle(const Date &date);
	// 显示账户信息
	void show() const;
};

#endif