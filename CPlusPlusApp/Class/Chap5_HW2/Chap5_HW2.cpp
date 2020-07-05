#include <iostream>
using namespace std;

class Mouse {
    static int num;
    public:
        Mouse() { num++; }
        Mouse(Mouse &p) { num++; }
        ~Mouse() { num--; }
};

void fn(Mouse m);

int Mouse::num = 0;

int main()
{
    Mouse a;
    cout << Mouse::num << endl;
    Mouse b(a);
    cout << Mouse::num << endl;
    for (int i = 0; i < 10; ++i)
    {
        Mouse x;
        cout << Mouse::num << endl;
    }
    fn(a);
    cout << Mouse::num << endl;
    return 0;
}

void fn(Mouse m)
{
    cout << Mouse::num << endl;
    Mouse n(m);
    cout << Mouse::num << endl;
}