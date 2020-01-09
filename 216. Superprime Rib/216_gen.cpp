
#include<iostream>
#include<cstdio>
#include<fstream>
#include<cmath>

int N;
int a[]={2,3,5,7};
//�ж��Ƿ�Ϊ����
int prime(int n){
    if(n==2)return 1;
    if(n%2==0)return 0;
    for(int i=3;i*i<=n;i++){
        if(n%i==0)return 0;
    }
    return 1;
}
//�������ж�
void dfs(int i,int j){
    if(!prime(i)||j>N)return ;//���i������������j����N�޷���ֵ
    if(j==N&&prime(i))printf("%d\n",i);//�����������j==N;���ӡ
    for(int k=1;k<=9;k+=2){//ĩλΪż���Ķ������������ÿ���
        dfs(i*10+k,j+1);
    }
}
int main(){
    while(scanf("%d",&N))
        for(int i=0;i<4;i++){
            dfs(a[i],1);
        }
}
