#include <stdlib.h>
#include <stdio.h>

int min_sub_arr(int* arr, int len){
    int* sum = malloc((len+1)*sizeof(int));
    sum[0] = 0;
    int i = 0;
    int min_sum = 1<<(sizeof(int)*8-1)-1; //MAX int
    int max_sum = 1<<(sizeof(int)*8-1);
    for(i = 1; i < len+1; i++) {
        sum[i] = sum[i-1]+arr[i];
        if(sum[i] < min_sum){
            min_sum = sum[i];
        }
        if(sum[i]> max_sum){
            max_sum = sum[i];
        }

    }
    free(sum);
    return max_sum - min_sum;
}

int min_sub_arr_two(int a[], int size) {
    int sum = 0;
    int max = 1<<31 -1; //Force it to overflow
    int cur = 0;
    while(cur < size) {
        sum +=a[cur++];
        if(sum > max) {
            max = sum;
        } else if(sum < 0) {
            sum  = 0;
        }
    }
    return max;

}

int main() {
    int arr[] = {1,-2,3,10,-4,7,2,-5};
    printf("%d\n", min_sub_arr(arr, 8));

}
