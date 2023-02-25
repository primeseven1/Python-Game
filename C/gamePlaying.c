// This file contains other conditions to end the game if one of the other files hasn't specified that
#include "./Error/errorWindow.h"

void enemyPastPlayer(int* gamePlaying, const float enemyCenterY)
{
    if (!gamePlaying) 
    {
        errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"gamePlaying\"");
        return;
    }

    if (enemyCenterY < 0) *gamePlaying = 0;
}

void playerCrashIntoEnemy(int* gamePlaying)
{
    if (!gamePlaying) 
    {
        errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"gamePlaying\"");
        return;
    }

    *gamePlaying = 0;
}