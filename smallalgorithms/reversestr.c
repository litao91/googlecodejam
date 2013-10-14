#include <stdio.h>
#include <string.h>

void reverseFixlen(char *str, int n) {
    char* p = str+n-1;
    while (str < p) {
        char c = *str;
        *str = *p; *p=c;
        str++;
        p--;
    }
}

void reverse(char *str) {
    reverseFixlen(str, strlen(str));
}

void main() {
    char hello[] = "helloworld";
    reverse(hello);
    printf("%s\n", hello);
}
