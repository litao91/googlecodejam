#include <stdlib.h>
#include <stdio.h>
static int* stack = NULL ;
static int top = 0;
void print_combination(int n) {
    //Initialize the stack at the first time
    if (stack == NULL) {
        stack = malloc(sizeof(int)*n);
    }
    if(n <= 0 && top >=2) {
        int i = 0;
        for(i=0; i<top; i++) {
            printf("%d, ", stack[i]);
        }
        printf("\n");
        return;
    } else if(n <=0) {
        return;
    }

    stack[top++] = n;
    print_combination(n-1);
    top--;
    print_combination(n-1);
}

int main() {
    print_combination(16);
    free(stack);
}
