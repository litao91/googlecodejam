#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void reverse_char(char* str, int start, int end) {
    printf("i = %d, j = %d\n", start, end);
    int i = start;
    int j = end;
    char tmp;
    for(; i<j; i++, j--) {
        tmp = str[i] ;
        str[i] = str[j];
        str[j] = tmp;
    }
}

void reverse_sentence(char* str, char stop_char ) {
    int len = strlen(str);
    reverse_char(str, 0, len-1);
    int i = -1;
    int j = 0;
    while(1){
        while(i < len && (i!=-1 &&str[i]!=stop_char) ) i++;
        if(i < len)
            j = i+1;
        else
            break;
        while(j < len && str[j]!=stop_char) j++;
        reverse_char(str, i+1, j-1);
        if(j>=len) break;
        i = j;
        j++;
    }
}


int main() {
    char* tst = "This is a short sentence to test the program";
    char* mutable = malloc(sizeof(char*)*strlen(tst));
    strcpy(mutable, tst);
    printf("%s\n", mutable);
    reverse_sentence(mutable, ' ');
    printf("%s\n", mutable);
    free(mutable);
}
