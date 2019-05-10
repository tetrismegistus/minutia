#include <stdio.h>

/* Verify that the expression getchar() != EOF is 0 or 1 */

int main() {
    int c;
    c = getchar() != EOF;
    printf("%d\n", c);
}
