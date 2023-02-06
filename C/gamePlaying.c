// This file contains other conditions to end the game if one of the other files hasn't specified that

void enemyPastPlayer(int* gamePlaying, const float enemyCenterY)
{
    if (enemyCenterY < 0) *gamePlaying = 0;
}

void playerCrashIntoEnemy(int* gamePlaying)
{
    *gamePlaying = 0;
}