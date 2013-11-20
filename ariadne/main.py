import random

import cog

back_id = None

MAX_BLOCKS = 20

def block_init(btype, x, y):
    if btype == 'm':
        block_id = cog.sprite_add("media/block.png")
        block = cog.sprite_get(block_id)
        block.dim.w = 0.05
        block.dim.h = 0.05
        block.pos.x = block.dim.w * 2 * x + (block.dim.w) - 1.0
        block.pos.y = block.dim.h * 2 * y + (block.dim.h) - 1.0


def game_init():
    #back
    back_id = cog.sprite_add("media/back.png")
    back = cog.sprite_get(back_id)
    back.dim.w = 1.0
    back.dim.h = 1.0

    #blocks
    with open('media/level00.lvl') as lvlfile:
        x = 0
        y = MAX_BLOCKS - 1
        for line in lvlfile:
            for c in line:
                block_init(c, x, y)
                x += 1
            y -= 1
            x = 0


def game_mainloop():
    pass


if __name__ == "__main__":
    cog.init()
    game_init()
    while not cog.hasquit():
        cog.loopstep()
        game_mainloop()
    cog.quit()
