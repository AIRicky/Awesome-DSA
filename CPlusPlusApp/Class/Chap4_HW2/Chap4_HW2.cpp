/* students please write your program here */

#include <iostream>
using namespace std;

class Integer {
private:
    int _num;
    //getLength()函数获取_num长度
    int getLength();
public:
    //Integer类构造函数
    Integer(int num) :_num(num) {
    };
    //反转_num
    int inversed();
};

int Integer::getLength() {
    int base = 10;
    int length = 1;
    while (_num / base != 0) {
        length += 1;
        base *= 10;
    }
    return length;
}

int Integer::inversed() {
    int reversedNum = 0, iterNum;
    iterNum = getLength();
    for (int i = 0; i < iterNum; i++) {
        reversedNum *= 10;
        reversedNum += _num % 10;
        _num /= 10;
    }
    return reversedNum;
}

int main() {
    int n;
    cin >> n;
    Integer integer(n);
    cout << integer.inversed() << endl;
    return 0;
}
