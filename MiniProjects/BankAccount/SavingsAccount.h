#ifndef SAVINGSACCOUNT_H_
#define SAVINGSACCOUNT_H_
#include "Date.h"
#include <string>

#pragma once
class SavingsAccount
{ // �ʴ��˻���
private:
	std::string id; // �˺�
	double balance; // ���
	double rate; // ���������
	Date lastDate; // �ϴα����������
	double accumulation; // �����ۼ�֮��
	static double total; // �����˻����ܽ��
	// ��¼һ���ˣ�dateΪ���ڣ� amountΪ���  
	void record(const Date &date, double amount, const std::string &desc);
	void error(const std::string& msg) const;
	double accumulate(Date date) const {
		return accumulation + balance * date.distance(lastDate);
	}

public:
	// ���캯��
	SavingsAccount(const Date &date, const std::string &id, double rate);
	const std::string getId() const { return id; }
	double getBalance() const { return balance; }
	double getRate()const { return rate; }
	static double getTotal() { return total;}

	// �����ֽ�
	void deposit(const Date &date, double amount, const std::string &desc);
	// ȡ���ֽ�
	void withdraw(const Date &date, double amount, const std::string &desc);
	// ������Ϣ
	void settle(const Date &date);
	// ��ʾ�˻���Ϣ
	void show() const;
};

#endif