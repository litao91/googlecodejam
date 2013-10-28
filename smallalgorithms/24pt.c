#include <stdlib.h>
#include <string.h>
#include <stdio.h>
char** expr;

void swap(int* arr, int i, int j) {
    int x = arr[i];
    arr[i] = arr[j];
    arr[j] = x;
}

void swap_str(char** arr, int i, int j) {
    char* x = arr[i];
    arr[i] = arr[j];
    arr[j] = x;
}
void solve24pt(int* arr, int start, int end, int target) {
    int i,j;
//    printf("start = %d, end = %d\n", start, end);
    /*for(i = start; i < 4; i++) {*/
        /*printf("%d ", arr[i]);*/
    /*}*/
    /*printf("\n");*/

    if(start == end) {
        if(target == arr[start]) {
            printf("%s\n", expr[start]);
        }
        return;
    }
    for(i = start; i < end; i++) {
        for(j = i+1; j<=end; j++) {
            int var_1 = arr[i];
            int var_2 = arr[j];
            char expr1[50];
            char expr2[50];
            strcpy(expr1, expr[i]);
            strcpy(expr2, expr[j]);
            swap(arr,j,end);
            swap_str(expr, j, end);

            arr[i] = var_1+var_2;
            sprintf(expr[i],"(%s + %s)", expr1, expr2);
            solve24pt(arr, start, end-1, target);

            arr[i] = var_1*var_2;
            sprintf(expr[i],"(%s * %s)",expr1, expr2);
            solve24pt(arr, start, end-1, target);

            arr[i] = var_1-var_2;
            sprintf(expr[i],"(%s - %s)",expr1, expr2);
            solve24pt(arr, start, end-1, target);

            if(var_2!=0) {
                arr[i] = var_1/var_2;
                sprintf(expr[i],"(%s / %s)",expr1, expr2);
                solve24pt(arr, start, end-1, target);
            }

            arr[i] = var_1;
            swap(arr, j,end);
            swap_str(expr, j, end);
            strcpy(expr[i], expr1);
        }
    }
}

int main() {
    int n = 4;
    int arr[] = {11,8,3,5};
    expr = malloc(sizeof(char*)*n);
    int i;
    for(i = 0; i < n; i++) {
        expr[i] = malloc(sizeof(char)*50);
        sprintf(expr[i], "%d",arr[i]);
    }
    solve24pt(arr, 0, 3, 24);


    for(i = 0; i < n; i++) {
        free(expr[i]);
    }
    free(expr);
}

