#include <stdio.h>
int cntof1(int n) {
    //A length of 10 is enough for a 32 bit integer
    int prefix[10];
    int suffix[10];
    int digit[10];
    int i = 0;
    int base = 1;
    while(base < n) {
        suffix[i] = n % base;
        digit[i]  = ((n % (base*10))-suffix[i])/base;
        prefix[i] = (n-suffix[i] - digit[i]*base)/(base*10);
        i++;
        base*=10;
    }

    int count = 0;
    int j = 0;
    base = 1;
    for( j = 0; j<i;j++) {
        if(digit[j]<1) {
            count += prefix[j] * base;
        } else if (digit[j] == 1) {
            count += prefix[j]*base+suffix[j]+1;
        } else {
            count += (prefix[j]+1)*base;
        }
        base*=10;
    }
    return count;
}

int main() {
    printf("%d\n", cntof1(12));
}
