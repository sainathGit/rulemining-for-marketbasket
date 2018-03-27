#include <iostream>
#include <math.h>
using namespace std;

int main() {
	
	int n, k, cells1, r1, r2, cells2;
	cin >> n >> k;

	if (n == 0) {
		cout << 0 << endl;
		return 0;
	}

	cells1 = ceil(float(n)/2);
	cells2 = cells1 - 1;
	r1 = n%k;
	r2 = k - r1;


	cout << (r1*cells1*(cells1 - 1)/2) + (r2*cells2*(cells2 - 1) / 2) << endl;




	return 0;
}