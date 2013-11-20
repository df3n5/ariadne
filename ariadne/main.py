import random

import cog

back_id = None

def game_init():
    back_id = cog.sprite_add("media/back.png")
    back = cog.sprite_get(back_id)
    back.dim.w = 1.0
    back.dim.h = 1.0


def game_mainloop():
    pass


if __name__ == "__main__":
    cog.init()
    game_init()
    while not cog.hasquit():
        cog.loopstep()
        game_mainloop()
    cog.quit()
