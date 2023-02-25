// Rather than just crashing, it will pop up an error window, and then stop working
#include <string.h>
#include "errorWindow.h"

void errorWindow(const int errorType, const LPCSTR errorInfo)
{
    LPCSTR caption;

    switch(errorType)
    {
    case DEREFERENCE_NULL_POINTER:
        caption = "Dereference NULL Pointer Error";
        break;
        
    case FILE_NOT_FOUND:
        caption = "File Not Found Error";
        break;

    default:
        caption = "Unknown error";
        break;
    }

    MessageBoxA(NULL, errorInfo, caption, MB_OK | MB_ICONERROR);
}