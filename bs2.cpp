#include<iostream>
using namespace std;

int main() {
    int a, b;
    int sum = 0;
    cin >> a >> b;

    for (int i = a; i < b; i++) {
        cout << i << " + ";
        sum += i;
    }
    sum += b;
    cout << b << " = " << sum;

    return 0;
}