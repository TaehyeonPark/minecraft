#include <iostream>
#include <vector>
#include <stdlib.h>

using namespace std;

typedef struct mca{
    int x;
    int z;

    double M32(int n){return n<<5;}
    double D32(int n){return n/32.0;}
    double S5(int n){return n>>5;}    
} mca;

int main(int argc, char *argv[]){
    cin.tie(0);
    ios::sync_with_stdio(false);
    
    while (1)
    {
        cout << "r.x.z.mca >> " << flush;
        char *p = (char *)malloc(sizeof(char)*100);
        cin >> p;
        if (p[0] == 'q') break; /* halt */

        mca r;
        vector<int> idx;
        cout << "p: " << p << endl;
        int i = 0;
        while (*p != '\0'){
            if (*p == '.'){
                idx.push_back(i);
            }
            p++;
            i++;
        }
        p = p - i;

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

        r.x = atoi(x.data());
        r.z = atoi(z.data());

        cout << "M32: " << r.M32(r.x) << endl;
        cout << "M32: " << r.M32(r.z) << endl;
        cout << "/tp @s " << r.M32(r.x) << " ~ " << r.M32(r.z) << endl;
    }
    
    return 0;
}
