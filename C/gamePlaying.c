// This file contains other conditions to end the game if one of the other files hasn't specified that
#include "./Error/errorWindow.h"
#include "save.h"

void playerCrashIntoEnemy(int* gamePlaying, const int score)
{
    if (!gamePlaying) 
    {
        errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"gamePlaying\"");
        return;
    }

    *gamePlaying = 0;
    saveScore(score);
}

/* This variable and function is being used so that the "enemyPastPlayer" function knows what the score is, and it can use it
   the caller that's in the enemy sprite class does not have access to the score, so the window class will call this function to update it */
static int currentScore;
void setScore(const int score) { currentScore = score; }

void enemyPastPlayer(int* gamePlaying, const float enemyCenterY)
{
    if (!gamePlaying) 
    {
        errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"gamePlaying\"");
        return;
    }

    if (enemyCenterY < 0)
    {
        *gamePlaying = 0;
        saveScore(currentScore);
    }
}