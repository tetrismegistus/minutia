#include <stdio.h>

/*
 * Write a program to print a histogram of the frequencies of different characters in its
 * input.
 */

#define FIRSTCHAR 33
#define LASTCHAR  94
int main(void) {
    /* considers ASCII 33 - 127
       if index 0 correspondes to char 33 - then
       0 + 33 = char
       1 + 33 = char
       2 + 33 = char
       ... to 94 */

    int i, c, v, h, maxoccurence;
    int hist[LASTCHAR];

    maxoccurence = 0;

    for (i = 0; i < LASTCHAR; ++i)
        hist[i] = 0;

    while ((c = getchar()) != EOF)
        ++hist[c - FIRSTCHAR]; /* because 33 is the offset from 0 of the first ASCII char */

    for (i = 0; i < LASTCHAR; ++i) {
        if (maxoccurence < hist[i])
            maxoccurence = hist[i];
    }

    /* vertical axis */
    for (v = maxoccurence; v > 0; --v) {
        printf("%2d", v);
        /* horizontal axis */

        for (h = 0; h < LASTCHAR; ++h) {
            if ((hist[h] > 0) && (hist[h] >= v))
                printf(" +");
            else if (hist[h] > 0)
                printf("  ");
        }

        printf("\n");
    }

    /*label h axis */
    printf("   ");
    for (h = 0; h < LASTCHAR; ++h) {
        if (hist[h] > 0)
            printf("%c ", h + FIRSTCHAR);
    }
    printf("\n");
}
