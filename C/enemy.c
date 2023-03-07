#include <stdlib.h>

// Return value stuff
enum FunctionCalls
{
    DONT_SHOOT,
    SHOOT
};

int enemyShoot(const unsigned int windowHeight, const float enemyCenterY, const unsigned int chances)
{
    if (rand() % chances == 0 && enemyCenterY < windowHeight) return SHOOT;
    return DONT_SHOOT;
}