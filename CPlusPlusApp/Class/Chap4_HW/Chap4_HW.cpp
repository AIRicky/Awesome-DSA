/* students please write your program here */

#include <iostream>
using namespace std;
class Integer {
private:
    int _num;
public:
    //构造函数
    Integer(int num) {
        _num = num;
    }
    //查询Integer数值
    int getNum() {
        return _num;
    }
    //计算当前Integer 和 b之间的最大公约数
    int gcd(Integer b) {
        int value = b.getNum();
        int minNum = _num > value ? value:_num;
        while (minNum >= 1)
        {
            if ((_num%minNum) + (value% minNum) ==0)
                break;
            minNum--;
        }
        return minNum;
    }
};
int main() {
    int a, b;
    cin >> a >> b;
    Integer A(a);
    Integer B(b);
    cout << A.gcd(B) << endl;
    return 0;
}
