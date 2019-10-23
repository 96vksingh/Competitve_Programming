#include<bits/stdc++.h>
using namespace std;
int main() {

    int n;
    cin>>n;
    int a[n];
    for(int i =0;i<n;i++)
    {
        cin>>a[i];
    }
    int k;
    cin>>k;
    int m;
    cin>>m;
  
    
    for(int i =0;i<m;i++)
    {
        int y,z;
        cin>>y>>z;
        int sum = 0;
        for(int j =y-1;j<z;j++)
        sum+=a[j];
        
        cout<<sum*k<<endl;
    }
    return 0;
	// Write your code here
}
