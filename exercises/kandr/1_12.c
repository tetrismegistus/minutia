#include <stdio.h>

/*
 * Write a program that prints its input one word per line.
 */

#define IN  1  /* inside a word */
#define OUT 2  /* outside a word */


/* count lines, words, and characters in input */
int main () {
    int c, state;

    state = OUT;

    while ((c = getchar()) != EOF) {

        if (c == ' ' || c == '\n' || c == '\t') {
            state = OUT;
        } else if (state == OUT) {
            state = IN;
            putchar('\n');
            putchar(c);
        } else {
            putchar(c);
        }
    }
}