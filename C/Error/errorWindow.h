#pragma once

#include <Windows.h>

enum ErrorCodes
{
    DEREFERENCE_NULL_POINTER = 1,
};

void errorWindow(const int errorType, const LPCSTR errorInfo);