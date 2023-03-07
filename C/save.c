#include <stdio.h>
#include <time.h>
#include "Error/errorWindow.h"
#include "save.h"

void saveScore(const int score)
{
    // I honestly don't really care about reading from the file, too many issues can come with that
    // Opening the file in append mode
    FILE* saveFile;
    saveFile = fopen("saveFile.txt", "a");

    if (!saveFile) 
    {
        errorWindow(CANNOT_SAVE, "Cannot open the file to save the score");
        return;
    }

    // Adding the time to the save
    time_t rawTime;
    struct tm* timeInfo;
    char currentTime[80];

    time(&rawTime);
    timeInfo = localtime(&rawTime);

    // Format the time as a string
    strftime(currentTime, sizeof(currentTime), "%Y-%m-%d %H:%M:%S", timeInfo);

    // Checking how much info is in the file
    fseek(saveFile, 0, SEEK_END);
    int size = ftell(saveFile);

    // If the file is empty, it doesn't do a new line
    if (size == 0) 
    {
        if (fprintf(saveFile, "%s Score: %i", currentTime,  score) < 0)
        {
            fclose(saveFile);
            errorWindow(CANNOT_SAVE, "Error while writing score to file");
            return;
        }
    }
    else if (fprintf(saveFile, "\n%s Score: %i", currentTime, score) < 0) 
    {
        fclose(saveFile);
        errorWindow(CANNOT_SAVE, "Error while writing score to file");
        return;
    }

    fclose(saveFile);
}