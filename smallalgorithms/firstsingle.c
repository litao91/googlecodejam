#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char first_single(char* str) {
    int len = strlen(str);
    int dict[255];
    memset(dict, 0, 255*sizeof(int));
    int i = 0;
    for(i = 0; i < len; i++) {
        dict[str[i]]++;
    }
    for(i = 0; i<len; i++) {
        if(dict[str[i]] == 1) {
            return str[i];
        }
    }
    return '\0';
}

int main() {
    char* str = "abaccdeff";
    printf("%c\n", first_single(str));
}
