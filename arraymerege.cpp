#include<iostream>
using namespace std;

int main(){
    int x[5] = {2, 4, 6, 8, 10};
    int y[5] = {1, 3, 5, 7, 9};
    int z[10];

    for(int i = 0; i<10; i++){
        z[i] = x[i]+y[i];
    }

    for(int i = 0; i<10; i++){
        cout<<z[i]<<" ";
    }
}
