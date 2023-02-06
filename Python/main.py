import window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    game_window = window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Game")
    window.c_functions.setSeed()
    game_window.setup()
    game_window.run()

if __name__ == "__main__":
    main()
