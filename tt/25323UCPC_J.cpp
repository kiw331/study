#include <iostream> 
#include <cmath>
using namespace std; 

long long  *arr;
long long  *sorted;

void parr(int n){
    for (int i = 0; i < n; i++) { 
        cout << arr[i] <<" "; 
    } 
    cout << '\n';
}

// 제곱수인지 확인
bool issq(long long n){

    int od= n%10;
    if ((od==2) || (od==3) || (od==7) || (od==8)){
        return false;
    }

    double a =sqrt(n);
    if (fmodf(a,1)==0){
        return true;
    }
    return false;

}

void quickSort(int i, int j){
	if(i>=j) return;
	long long pivot = sorted[(i+j)/2];
	int left = i;
	int right = j;
	
	while(left<=right)
	{
		while(sorted[left]<pivot) left++;
		while(sorted[right]>pivot) right--;
		if(left<=right)
		{
			swap(sorted[left],sorted[right]);
			left++; right--;
		}
	}
	quickSort(i,right);
	quickSort(left,j);
}

int main() { 
    int n;
    long long min; 
    cin >> n; 

    arr = new long long[n];
    sorted = new long long[n];

    for (int i = 0; i < n; i++) { 
        cin >> arr[i]; 
        sorted[i] = arr[i];
    } 

    quickSort(0,n-1);

    for (int i=0; i<n; i++){
        
        if (i==n-1){
            cout << "YES";
            break;
        }

        min = sorted[i];
        int min_idx;


        if(issq(arr[i]*min)){
            //최소값 인덱스
            for (int j=i; j<n; j++){
                if (arr[j]==min){
                    min_idx = j;
                    break;
                }
            }
            if (min_idx == i)   continue;

            arr[min_idx] = arr[i];
            arr[i] = min;
        }
        else {
            cout << "NO";
            break;
        }
    }

    return 0;
}