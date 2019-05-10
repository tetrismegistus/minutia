#include <stdio.h>

/* Write a program to count blanks, tabs, and newlines */

int main(void) {
    int c, nt, nl, nb;
    nt = 0;
    nl = 0;
    nb = 0;

    while ((c = getchar()) != EOF)
        if (c == '\t') {
            ++nt;
        } else if (c == '\n') {
            ++nl;
        } else if (c == ' ') {
            ++nb;
        }

    printf("%d tabs, %d newlines, %d blanks\n", nt, nl, nb);
}