#include <string.h>
#include "errorWindow.h"

// Rather than the game just not working correctly, it will give you an error window :D
void errorWindow(const int errorType, const LPCSTR errorInfo)
{
    LPCSTR windowTitle;

    // Adding the second part of the error to the error info
    char error2[] = "\n\nYou can continue, but the program will not work correctly";
    char* fullError = (char*)malloc(strlen(errorInfo) + strlen(error2) + 1);
    if (!fullError) return;

    strcpy_s(fullError, strlen(fullError) + strlen(errorInfo) + 1, errorInfo);
    strcat_s(fullError, strlen(fullError) + strlen(error2) + 1, error2);

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

    MessageBoxA(NULL, fullError, windowTitle, MB_OK | MB_ICONERROR);
    
    free(fullError);
    fullError = NULL;
}
