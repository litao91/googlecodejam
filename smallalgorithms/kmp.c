#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void overlay(char* str, int len, int** idx) {
    *idx = malloc(sizeof(int)*len); //record the overlay length
    int* overlay_idx = *idx;
    memset(overlay_idx, -1, sizeof(int)*len);
    overlay_idx[0] = -1; //-1 means no overlay at all
    int i = 1;
    for(i = 1; i < len; i++) {
        int overlay_pos = overlay_idx[i-1];
        while(1) {
            if(str[i] == str[overlay_pos+1]) { //compare with the next element of overlay
                overlay_idx[i] = overlay_idx[i-1]+1;
                break;
            } else if(overlay_pos >= 0) {
                overlay_pos = overlay_idx[overlay_pos];
            }else{
                break;
            }
        }
    }
}


int main() {
    int* idx;
    char* str = "abcabc";
    overlay(str, 6, &idx);
    int i = 0;
    for(i=0; i<6;i++) {
        printf("%d ", idx[i]+1);
    }
    printf("\n");

}

