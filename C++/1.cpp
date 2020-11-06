#include <iostream>
using namespace std;

int main(){
	int a, jumlah, jumlah1, rata;
	int A[20];
	cin >> a;
	for (int i=0;i<a;i++){
		cin >> A[i];
	}
	for (int i=0; i<a; i++){
		jumlah+=A[i];
	}
	rata=jumlah/a;
	jumlah1=0;
	for (int i=0;i<a;i++){
		if (A[i]>rata){
			jumlah1=A[i];
		}
	}
	cout<<"hasil : "<<jumlah1;
}
