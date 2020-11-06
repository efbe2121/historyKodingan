#include <iostream>
using namespace std;

int main(){
    int n,i,max1,max2,min1,min2;
    cout << "Masukkan banyak n : "<<endl;
    cin >> n;
    
    int A[n];
    cout << "Masukkan bilangan: "<<endl;
    
    for (i=0;i<n;i++){
    	cin >> A[i];
    }
    max1 = (A[0]>A[1]) ? A[0] : A[1];
    max2 = (A[0]>A[1]) ? A[1] : A[0];
    
    for (i=2;i<n;i++){
    	if (A[i] > max1){
    		max2 = max1;
    		max1 = A[i];
    	}else if (A[i]>max2){
    		max2 = A[i];
    	}
    }
    
    min1 = (A[0]<A[1]) ? A[0] : A[1];
    min2 = (A[0]<A[1]) ? A[1] : A[0];
    
    for (i=2;i<n;i++){
    	if (A[i]<min1){
    		min2 = min1;
    		min1 = A[i];
    	}else if (A[i]<min2){
    		min2 = A[i];
    	}
    }
    
    cout << "Bilangan terbesar kedua: "<<max2<<endl;
    cout << "Bilangan terkecil kedua: "<<min2<<endl;
    
}
