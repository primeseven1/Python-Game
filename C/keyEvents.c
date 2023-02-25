#include "./Error/errorWindow.h"

#define RUN_SETUP 1
#define SHOOT 2

enum keyCodes {
    KEY_CODE_SPACE = 32,
    KEY_CODE_A = 97,
    KEY_CODE_D = 100,
    KEY_CODE_LEFT = 65361,
    KEY_CODE_RIGHT = 65363,
    KEY_CODE_ENTER = 65293,
    KEY_CODE_ESCAPE = 65307
};

int keyPressed(const int* key, int* moveLeft, int* moveRight, int* gamePlaying)
{
    if (!key || !moveLeft || !moveRight || !gamePlaying)
    {
        if (!key) errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"key\"");
        if (!moveLeft) errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"moveLeft\"");
        if (!moveRight) errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"moveRight\"");
        if (!gamePlaying) errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"gamePlaying\"");

        return 0;
    }

    if (!*gamePlaying && *key == KEY_CODE_ENTER) 
    {
        *gamePlaying = 1;
        return RUN_SETUP;
    }

    if (*gamePlaying)
    {
        switch(*key)
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

void keyReleased(const int* key, int* moveLeft, int* moveRight)
{
    if (!key || !moveLeft || !moveRight)
    {
        if (!key) errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"key\"");
        if (!moveLeft) errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"moveLeft\"");
        if (!moveRight) errorWindow(DEREFERENCE_NULL_POINTER, "Attempted to dereference NULL pointer \"moveRight\"");

        return;
    }

    switch(*key)
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