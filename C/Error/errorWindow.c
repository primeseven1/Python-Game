// Rather than just crashing, it will pop up an error window, and then stop working
#include <string.h>
#include "errorWindow.h"

void errorWindow(const int errorType, const LPCSTR errorInfo)
{
    LPCSTR windowTitle;

    // I will probably add more error codes later, but file not found causes the window to completely stop working
    switch(errorType)
    {
    case DEREFERENCE_NULL_POINTER:
        windowTitle = "Dereference NULL Pointer Error";
        break;

    default:
        windowTitle = "Unknown error";
        break;
    }

    MessageBoxA(NULL, errorInfo, windowTitle, MB_OK | MB_ICONERROR);
}