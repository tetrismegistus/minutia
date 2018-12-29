#include <stdio.h>


/* How would you test the word count program? [LISTING BELOW]  What kinds of input are most likely to uncover bugs if
 * there are any?
 * 
 * I would throw very large files attempt to cause an overflow of any one of the ints being used to keep count\
 * I would also throw a mix of lots of whitespace and unprintable characters to try to confuse it
 */

#define IN  1  /* inside a word */
#define OUT 2  /* outside a word */


/* count lines, words, and characters in input */
int main () {
    int c, nl, nw, nc, state;

    state = OUT;
    nl = nw = nc = 0;
    while ((c = getchar()) != EOF) {
        ++nc;
        if (c == '\n')
            ++nl;
        if (c == ' ' || c == '\n' || c == '\t')
            state = OUT;
        else if (state == OUT) {
            state = IN;
            ++nw;
        }

    }
    printf("%d %d %d\n", nl, nw, nc);
}