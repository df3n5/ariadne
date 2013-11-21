import random

import cog

back_id = None

MAX_BLOCKS = 20
BLOCK_DIM = 1.0 / MAX_BLOCKS

class KeyCodes:
    W = 119
    A = 97
    S = 115
    D = 100


def block_init(btype, x, y):
    if btype == 'w':
        path = 'media/block.png'
    elif btype == 'E':
        path = 'media/goal.png'
    elif btype.strip() == '':
        return
    else:
        raise Exception("Invalid block type {}".format(btype))
    block_id = cog.sprite_add(path)
    block = cog.sprite_get(block_id)
    block.dim.w = BLOCK_DIM
    block.dim.h = BLOCK_DIM
    block.pos.x = block.dim.w * 2 * x + (block.dim.w) - 1.0
    block.pos.y = block.dim.h * 2 * y + (block.dim.h) - 1.0
    return block_id


def player_init(x, y):
    player_id = cog.sprite_add('media/player.png')
    player = cog.sprite_get(player_id)
    player.dim.w = BLOCK_DIM/2
    player.dim.h = BLOCK_DIM/2
    player.pos.x = BLOCK_DIM * 2 * x + (player.dim.w) - 1.0
    player.pos.y = BLOCK_DIM * 2 * y + (player.dim.h) - 1.0
    return player_id


def game_init():
    #back
    back_id = cog.sprite_add("media/back.png")
    back = cog.sprite_get(back_id)
    back.dim.w = 1.0
    back.dim.h = 1.0

    #blocks
    blocks = []
    with open('media/level00.lvl') as lvlfile:
        x = 0
        y = MAX_BLOCKS - 1
        for line in lvlfile:
            for c in line:
                b = block_init(c, x, y)
                if not b is None:
                    blocks.append(b)
                x += 1
            y -= 1
            x = 0
    p = player_init(0, 18)
    return (p, blocks)


def game_mainloop(player_id, block_ids):
    player = cog.sprite_get(player_id)
    for b in block_ids:
        if(cog.sprite_collides_sprite(player_id, b)):
            print("Collision")
            #TODO: Response properly
            player.pos.x = player.pos.x - (player.vel.x * 10)
            player.vel.y = player.pos.y - (player.vel.y * 10)
            player.vel.x = 0
            player.vel.y = 0
            break
    if cog.input_key_pressed():
        key_code = cog.input_key_code_pressed()
        print("KEYCODE {}".format(key_code))
        vel_delta = 0.0001
        if key_code == KeyCodes.A:
            player.vel.x = -vel_delta
        if key_code == KeyCodes.D:
            player.vel.x = vel_delta
        if key_code == KeyCodes.W:
            player.vel.y = vel_delta
        if key_code == KeyCodes.S:
            player.vel.y = -vel_delta
    if cog.input_key_depressed():
        key_code = cog.input_key_code_depressed()
        print("KEYCODE DEPRESSED {}".format(key_code))
        if key_code == KeyCodes.A:
            player.vel.x = 0
        if key_code == KeyCodes.D:
            player.vel.x = 0
        if key_code == KeyCodes.W:
            player.vel.y = 0
        if key_code == KeyCodes.S:
            player.vel.y = 0


if __name__ == "__main__":
    cog.init()
    player_id, block_ids = game_init()
    while not cog.hasquit():
        cog.loopstep()
        game_mainloop(player_id, block_ids)
    cog.quit()
