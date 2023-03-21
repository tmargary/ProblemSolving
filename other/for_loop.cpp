/*
Print triagles using a for loop
*/

#include <iostream>

void printTri1(int n){
    for (int i=1; i<=n; i++){
        for (int j=1; j<=i; j++){
            std::cout << '*';
        }
        std::cout << std::endl;
    }
}

void printTri2(int n){
    for (int i=n; i>0; i--){
        for (int j=1; j<=i; j++){
            std::cout << '*';
        }
        std::cout << std::endl;
    }
}

void printTri3(int n){
    for (int i=n; i>0; i--){

        for (int j=1; j<i; j++){
            std::cout << ' ';
        }

        for (int j=1; j<=n-i+1; j++){
            std::cout << '*';
        }

        std::cout << std::endl;
    }
}

void printTri4(int n){
    for (int i=n; i>0; i--){

        for (int j=0; j<n-i; j++){
            std::cout << ' ';
        }

        for (int j=0; j<i; j++){
            std::cout << '*';
        }

        std::cout << std::endl;
    }
}

void printTri5(int n){

    int mid = n / 2;
    for (int i=n; i>0; i--){

        for (int j=1; j<=i-1; j++){
            std::cout << ' ';
        }

        for (int j=1; j<=n-i+1; j++){
            std::cout << '*';
        }

        for (int j=0; j<=n-i-1; j++){
            std::cout << '*';
        }

        std::cout << std::endl;
    }
}

void printTri6(int n){

    int mid = n / 2;
    for (int i=1; i<=n; i++){

        for (int j=1; j<i; j++){
            std::cout << ' ';
        }

        for (int j=1; j<=n-i+1; j++){
            std::cout << '*';
        }

        for (int j=0; j<n-i; j++){
            std::cout << '*';
        }

        std::cout << std::endl;
    }
}


int main(){
    int n = 5;

    printTri1(n);
    std::cout << std::endl;

    printTri2(n);
    std::cout << std::endl;

    printTri3(n);
    std::cout << std::endl;

    printTri4(n);
    std::cout << std::endl;

    printTri5(n);
    std::cout << std::endl;

    printTri6(n);
    std::cout << std::endl;
}
