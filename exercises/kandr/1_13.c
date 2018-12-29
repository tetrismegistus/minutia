#include <stdio.h>
/*
 * Write a program to print a histogram of the lengths of words in its input.
 * It is easy to draw the histogram with the bars horizontal; a vertical
 * orientation is more challenging
 */

#define IN  1
#define OUT 0

int main(void){
    int c, i, i2, nc, state, max_size;
    int hist[20];

    max_size = 0;
    nc = 0;
    state = OUT;

    /* initialize array */
    for (i = 0; i < 20; ++i)
        hist[i] = 0;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            state = OUT;
            ++hist[nc];
            nc = 0;
        }
        else if (state == OUT) {
            state = IN;
        }

        if (state == IN)
            ++nc;
    }

    /* get max word size */
    for (i = 0; i < 20; ++i) {
        if (hist[i] > max_size)
            max_size = hist[i];
    }

    for (i = max_size; i >= 1; --i) {
        printf("%d", i);

        for(i2 = 0; i2 < 20; ++i2) {
            if (hist[i2] >= i)
                printf(" + ");
            else
                printf("   ");
        }
        putchar('\n');
    }

    printf("  ");
    for (i = 0; i < 20; ++i)
        printf("%02d ", i);
    printf("\n");
}
