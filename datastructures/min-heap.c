#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define LEFT(i) (2*i+1)
#define RIGHT(i) (2*i+2)
#define PARENT(i) ((i-1)/2)

static int* heap;
static int heap_size;
void swap_int_arr(int * arr, int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}
int get_min_idx(int* arr, int i, int j) {
    return arr[i] < arr[j]? i:j;
}

void init_heap(int n){
    heap = malloc(sizeof(int)*n);
    memset(heap, 0, sizeof(int)*n);
}

void ran_heap(int k) {
    heap_size = k;
    int i;
    for(i = 0; i<k; i++) {
        heap[i] = rand();
    }
}

void heap_down(int* arr, int size, int t) {
    int min_idx = -1;
    if(RIGHT(t) < size) {
        min_idx = get_min_idx(arr, LEFT(t), RIGHT(t));
    } else if(LEFT(t) < size) {
        min_idx = LEFT(t);
    }else{ //don't have child
        return;
    }

    if(arr[min_idx] < arr[t]){ //child smaller than parent
        swap_int_arr(arr, t, min_idx);
        heap_down(arr, size, min_idx);
    }

}

void heap_up(int* arr, int size, int t) {
    if(t <= 0) {
        return;
    }
    int parent_idx = PARENT(t);
    if(arr[t] < arr[parent_idx]) {
        swap_int_arr(arr, t, parent_idx);
        heap_up(arr, size, parent_idx);
    }
}

int remove_min(int* arr, int* size) {
    if(*size <= 0) {
        return -1;
    }
    int min = arr[0];
    (*size)--;
    swap_int_arr(arr, 0, (*size));
    heap_down(arr, *size, 0);
    return min;
}

int insert(int* arr, int *size, int val) {
    arr[*size] = val;
    (*size)++;
    heap_up(arr, *size, *size-1);
}

int make_heap(int* arr, int size) {
    int j;
    for(j=size/2; j >= 0; j--) {
        heap_down(arr, size, j);
    }
}

int main() {
    init_heap(100);
    ran_heap(10);
    srand(time(NULL));
    make_heap(heap, 10);
    int i;
    for(i = 0; i<10; i++) {
        insert(heap, &heap_size, rand());
    }
    int n = heap_size;
    for(i = 0; i < n; i++) {
        printf("%d\n", remove_min(heap,&heap_size));
    }
}




