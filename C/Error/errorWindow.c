#include <string.h>
#include "errorWindow.h"

// Rather than the game just not working correctly, it will give you an error window :D
void errorWindow(const int errorType, const LPCSTR errorInfo)
{
    LPCSTR windowTitle;

    // I will probably add more error codes later, but file not found causes the window to completely stop working
    switch(errorType)
    {
    case DEREFERENCE_NULL_POINTER:
        windowTitle = "Dereference NULL Pointer Error";
        break;

    case CANNOT_SAVE:
        windowTitle = "Cannot save recent score";
        break;

    default:
        windowTitle = "Unknown error";
        break;
    }

    MessageBoxA(NULL, errorInfo, windowTitle, MB_OK | MB_ICONERROR);
}