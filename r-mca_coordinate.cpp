#include <iostream>
#include <vector>
#include <stdlib.h>
#include <tuple>

using namespace std;

#define EXIT_SIGNAL -1
#define EXIT_SUCCESS 0
#define EXIT_FAILURE 1

#define ERROR "Error    : "
#define EXIT "Exit     : "

#define INVALID "Invalid input"
#define HALT "halt"

typedef struct mca{
    int x;
    int z;
    char *p = (char *)malloc(sizeof(char)*100);

    char *getP(){return p;}
    char *setP(char *p){ 
        cin >> p;
        return p;
    }
    
    double M32(int n){return n<<5;}
    double D32(int n){return n/32.0;}
    double S5(int n){return n>>5;}

    int parser(char *p){
        vector<int> idx;
        int i = 0;
        if (p[0] == 'q' || p[0] == 'Q') {
            cout << "Exit" << endl;
            exit(EXIT_SIGNAL);
        }
        while (*p != '\0'){
            if (*p == '.'){
                idx.push_back(i);
            }
            p++;
            i++;
        }
        p = p - i;
        if (idx.size() < 3) {
            cout << ERROR << INVALID << endl;
            exit(EXIT_FAILURE);
        }
        vector<char> x;
        vector<char> z;

        for (int i = 0; i < sizeof(p); i++){
            if (i > idx[0] && i < idx[1]) {
                x.push_back(p[i]);
            }
            if (i > idx[1] && i < idx[2]) {
                z.push_back(p[i]);
            }
        }

        int iX = atoi(x.data());
        int iZ = atoi(z.data());

        cout << "M32: " << M32(iX) << endl;
        cout << "M32: " << M32(iZ) << endl;
        cout << "/tp @s " << M32(iX) << " ~ " << M32(iZ) << endl;
        return EXIT_SUCCESS;
    }
} mca;

int main(int argc, char *argv[]){
    cin.tie(0);
    ios::sync_with_stdio(false);

    while (1)
    {
        mca m;
        cout << "r.x.z.mca >> " << flush;
        m.setP(m.p);
        m.parser(m.p);    
    }
    
    return 0;
}
