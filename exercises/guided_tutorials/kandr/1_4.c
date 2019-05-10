#include <stdio.h>

/* Write a program to print the corresponding Celsus to Fahrenheit table */

int main() {
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;

    celsius = lower;

    printf("Cels\tFahrenheit\n");
    while (celsius <= upper) {
        /* T(°C) × 9/5 + 32 */
        fahr = celsius * (9.0/5.0) + 32;
        printf("%4.0f\t    %6.1f\n", celsius, fahr);
        celsius = celsius + step;
    }
}