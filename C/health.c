#include <stdlib.h>
#include <time.h>
#include "./Error/errorWindow.h"

enum Colors
{
    GREEN = 1,
    YELLOW,
    RED
};

void setSeed() 
{
    srand(time(0));
}

int subtractHealth(int* health, int* gamePlaying)
{
    if (!health || !gamePlaying)
    {
        if (!health) errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"health\"");
        if (!gamePlaying) errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"gamePlaying\"");
        
        return 0;
    }

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