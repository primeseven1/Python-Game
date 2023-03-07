#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "./Error/errorWindow.h"
#include "save.h"

// Based on return value determnines the color of the text
enum Colors
{
    GREEN = 1,
    YELLOW,
    RED
};

// Called once and only once
void setSeed() { srand(time(0)); }

// This function gets called every time thge player gets hit, it needs the score if the game ends
int subtractHealth(int* health, int* gamePlaying, const int score)
{
    // Checking for NULL pointers
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
        saveScore(score);
        return 0;
    }

    if (*health > 70) return GREEN;
    else if (*health > 40) return YELLOW;
    else return RED;
}