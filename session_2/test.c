#include <stdio.h>

int i;

void funzione(void)
{
    i=2;
    printf("%d\n", i);
}

void funzione_new(void)
{
    int i=20;
    printf("%d\n", i);
}

void main (void)
{
    i=1;
    printf("%d\n", i);
    funzione();
    printf("%d\n", i);
    funzione_new();
    printf("%d\n", i);
}