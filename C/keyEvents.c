#include "./Error/errorWindow.h"

// These are for functions that could be called based on a return value
enum FunctionCalls
{
    RUN_SETUP = 1,
    SHOOT = 2
};

enum keyCodes {
    KEY_CODE_SPACE = 32,
    KEY_CODE_A = 97,
    KEY_CODE_D = 100,
    KEY_CODE_LEFT = 65361,
    KEY_CODE_RIGHT = 65363,
    KEY_CODE_ENTER = 65293,
    KEY_CODE_ESCAPE = 65307
};

int keyPressed(const unsigned int key, int* moveLeft, int* moveRight, int* gamePlaying)
{
    // Not really liking the all the if statements too much, but i'm too lazy fix it
    // Checking for NULL pointers
    if (!moveLeft) 
    {
        errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"moveLeft\"");
        return 0;
    }
    if (!moveRight) 
    {
        errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"moveRight\"");
        return 0;
    }
    if (!gamePlaying) 
    {
        errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"gamePlaying\"");
        return 0;
    }

    // The enter key is what starts the game
    if (!*gamePlaying && key == KEY_CODE_ENTER) 
    {
        *gamePlaying = 1;
        return RUN_SETUP;
    }

    // Movement
    if (*gamePlaying)
    {
        switch(key)
        {
        case KEY_CODE_A:
        case KEY_CODE_LEFT:
            *moveLeft = 1;
            break;
        
        case KEY_CODE_D:
        case KEY_CODE_RIGHT:
            *moveRight = 1;
            break;

        case KEY_CODE_ESCAPE:
            *gamePlaying = 0;
            break;

        case KEY_CODE_SPACE:
            return SHOOT;
            break;
        }
    }

    return 0;
}

// This functions doesn't really care if the game is playing or not, and it doesn't need to
void keyReleased(const unsigned int key, int* moveLeft, int* moveRight)
{
    // Not really liking the all the if statements too much, but i'm too lazy fix it
    // Checking for NULL pointers
    if (!moveLeft) 
    {
        errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"moveLeft\""); 
        return;
    }
    if (!moveRight) 
    {
        errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"moveRight\"");
        return;
    }

    // Movement
    switch(key)
    {
    case KEY_CODE_A:
    case KEY_CODE_LEFT:
        *moveLeft = 0;
        break;
    
    case KEY_CODE_D:
    case KEY_CODE_RIGHT:
        *moveRight = 0;
        break;
    }
}