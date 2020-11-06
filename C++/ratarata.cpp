#include <iostream>
using namespace std;

int main(){
  int i,n,j,jml=0,cacah=0;

  cout << "Banyak data: ";cin>>n;
  int a[n];
  float rata;

  cout << "Bilangannya di input: "<<endl;
  for (i=0;i<n;i++){
    cin>>a[i];
    jml += a[i];
  }

  rata = jml/n;
  cout << "Rata-rata: "<<rata<<endl;

  for (i = 0;i<n;i++){
    if (a[i]>rata){
      cacah += a[i];
    }
  }

  cout << "Jmlh bilangan diatas rata-rata: "<<cacah<<endl;

}
