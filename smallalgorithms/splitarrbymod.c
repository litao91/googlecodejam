#include<stdio.h>
#include<stdlib.h>
void swap(int* arr, int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

int split(int* arr, int len) {
    int i = -1;
    int j = len;
    int k = 0;
    while(k<j){
        if(arr[k]%3 == 0) {
            i++;
            swap(arr,i,k);
        }else if(arr[k]%3==2) {
            j--;
            swap(arr,j,k);
        }else{
            k++;
        }

    }

}

int main() {
    int arr[]  = {1,2,3,4,5,6,7,8,9,10,11};
    split(arr, 11);
    int i =0;
    for(i =0; i<11;i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
