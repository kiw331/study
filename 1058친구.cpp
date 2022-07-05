#include<stdio.h>
#include <set>
using namespace std;


int main() {
    int n,f;
    int max = 0;
    char s[51][51];
    set<int> se;

    scanf("%d",&n);

    for (int i=0; i<n; i++) scanf("%s",s[i]);

    for (int i=0; i<n; i++){
        f =0;
        
        for (int j=0; j<n; j++){
            if (s[i][j]=='Y') {
                se.insert(j);

                //j의 친구 k도 se에 포함
                for (int k=0; k<n; k++){
                    if(k==i) continue; //자신일 경우
                    if (s[j][k]=='Y') se.insert(k);
                }
            }
        }
        // // 집합 원소 출력
        // for (auto i : se) cout << i << " ";
        //     printf("\n");

        f = se.size();
        if (f>max) max =f;
        se.clear();
    }
    printf("%d",max);

    return 0;
}