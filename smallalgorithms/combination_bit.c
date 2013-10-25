#include <stdio.h>
#include <stdlib.h>

static char* bit_flags = NULL;
static int size = -1;

#define INIT_BIT(n) bit_flags = malloc(sizeof(char)*(n/8+1))
#define SET_BIT(n, k) bit_flags[k/8] |= ((char)1) << (8-k%8)
#define CLEAR_BIT(n,k) bit_flags[k/8] &= ~((char)1<< (8-k%8))
#define GET_BIT(n,k) (bit_flags[k/8]&((char)1<< (8-k%8)))


void print_combination(int n) {
    if(bit_flags == NULL) {
        size = (n/8+1)*8;
        INIT_BIT(n);
    }

    //Initialize the stack at the first time
    if(n <= 0) {
        int i = 0;
        for(i = 0; i < size; i++) {

            if(GET_BIT(size, i)) {
                printf("%d, ", i+1);
            }
        }
        printf("\n");
        return;
    } else if(n <=0) {
        return;
    }

    SET_BIT(size, n);
    print_combination(n-1);
    CLEAR_BIT(size,n);
    print_combination(n-1);
}

int main() {
    print_combination(16);
    free(bit_flags);
}
