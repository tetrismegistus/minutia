#include <stdio.h>

/* Write a program to copy its input to its output, replacing each string of one or more blanks by a single blank. */

int main() {
    int c, nb;
    nb = 0;

    while ((c = getchar()) != EOF) {
        if (c == ' ') {
            ++nb;
        } else if (nb > 0) {
            putchar(' ');
            nb = 0;
            putchar(c);
        } else {
            putchar(c);
        }
    }
}