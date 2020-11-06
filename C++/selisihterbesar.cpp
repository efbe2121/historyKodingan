#include <iostream>
using namespace std;

int main(){

  int i,max1,max2,n,min1;
  cout << "Banyak n: "<<endl;cin>>n;
  int a[n];
  cout << "Masukkan bilangan: "<<endl;

  for (i=0;i<n;i++){
    cin >> a[i];
  }

  max1 = a[0]; max2 = a[0];
  for (i=0;i<n;i++){
    if (a[i]>max1){
      max1 = a[i];
    }
  }

  for (i=0;i<n;i++){
    if (a[i]>max2 && a[i]<max1){
      max2 = a[i];
    }
  }

  min1 = a[0];
  for (i=0;i<n;i++){
    if (a[i]<min1){
      min1 = a[i];
    }
  }

  cout << "Selisih terbesar kedua adalah: "<<max2-min1<<endl;

}
