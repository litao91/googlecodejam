#include <stdio.h>

// What the complier do
// 1. Make a copy of x
// 2. Do increment on the origin value
// 3. Assign the copy back to x
int main() {
    int x = 1;
    x = x++;
    printf("%d\n", x);
}
