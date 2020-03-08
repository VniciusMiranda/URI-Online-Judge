#include <iostream>


using namespace std;

int gcd(int divisor, int dividend){

	int c;

	while(dividend % divisor != 0){

		c = dividend % divisor;
		dividend  = divisor;
		divisor = c;
	}


	return divisor;
}

int main{

	int numb_test, b, a;
    	int mdc, smaller_value;

    	cin >> numb_test;

    	for(int i = 0; i < numb_test; i++){

        	cin >> a >> b;

        	if(a > b){

			divisor = b;
			dividend = a;
		}else{
	
			divisor = a;
			dividend = b;
		}
        }

        cout << gdc(divisor, dividend);
    }
	return 0;
}
