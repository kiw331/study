#include<iostream>
using namespace std;

int main() {
    int N;
    int sum = 0;
    cin >> N;

    for (int i = 1; i < N/2; i++) {
        if (N%i==0) { 
            cout << i << " + ";
            sum += i;
        }
    }
    sum += N/2;
    cout << N/2 << " = " << sum;

    return 0;
}