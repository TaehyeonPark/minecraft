#include <iostream>

using namespace std;

typedef struct mca{
    int x;
    int y;
} mca;
int main(int argc, char *argv[]){
    cin.tie(0);
    ios::sync_with_stdio(false);
    File *fp;
    
    //Directory listing
    fp = popen("ls -l", "r");
    if(fp == NULL){
        cout << "Error" << endl;
        return 1;
    }
    for (int i = 0; i < 10; i++){
        cout << fgetc(fp);
    }
    return 0;
}
