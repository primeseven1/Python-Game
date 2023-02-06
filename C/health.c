#include <stdlib.h>
#include <time.h>

#define GREEN 1
#define YELLOW 2
#define RED 3

void setSeed() 
{
    srand(time(0));
}

int subtractHealth(int* health, int* gamePlaying)
{
    *health -= rand() % (20 - 8) + 8;

    if (*health < 1) 
    {
        *gamePlaying = 0;
        return 0;
    }

    if (*health > 70) return GREEN;
    else if (*health > 40) return YELLOW;
    else return RED;
}