#include <stdio.h>

/* Modify the temperature conversion program to print a heading above the table*/

int main(){
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;      /* lower limit of temperature table */
    upper = 300;    /* upper limit */
    step = 20;      /* step size */

    printf("Fahr\tCelsius\n");

    fahr = lower;
    while (fahr <= upper) {
        celsius = (5.0 / 9.0) * (fahr - 32.0);
        printf("%4.0f\t %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
