import random

import cog

back_id = None

MAX_BLOCKS = 20
BLOCK_DIM = 1.0 / MAX_BLOCKS
p_x = 0
p_y = 18
start_pos_x = BLOCK_DIM * 2 * p_x + BLOCK_DIM - 1.0
start_pos_y = BLOCK_DIM * 2 * p_y + BLOCK_DIM - 1.0


class KeyCodes:
    W = 119
    A = 97
    S = 115
    D = 100
    UP = 1073741906
    DOWN = 1073741905
    LEFT = 1073741904
    RIGHT = 1073741903


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


def overlay_init(x, y):
    overlay_id = cog.sprite_add('media/overlay.png')
    overlay = cog.sprite_get(overlay_id)
    overlay.dim.w = 8.0
    overlay.dim.h = 8.0
    overlay.pos.x = x
    overlay.pos.y = y
    return overlay_id


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
    o = overlay_init(0, 0)
    p = player_init(0, 18)
    return (p, blocks, o)


def game_mainloop(player_id, block_ids, overlay_id):
    player = cog.sprite_get(player_id)
    overlay = cog.sprite_get(overlay_id)
    for b in block_ids:
        if(cog.sprite_collides_sprite(player_id, b)):
            print("Collision")
            player.pos.x = start_pos_x
            player.pos.y = start_pos_y
            '''
            #TODO: Response properly
            player.pos.x = player.pos.x - (player.vel.x * 10)
            player.vel.y = player.pos.y - (player.vel.y * 10)
            player.vel.x = 0
            player.vel.y = 0
            break
            '''
    if cog.input_key_pressed():
        key_code = cog.input_key_code_pressed()
        print("KEYCODE {}".format(key_code))
        vel_delta = 0.0001
        cam_vel_delta = 0.0005
        if key_code == KeyCodes.A:
            player.vel.x = -vel_delta
        if key_code == KeyCodes.D:
            player.vel.x = vel_delta
        if key_code == KeyCodes.W:
            player.vel.y = vel_delta
        if key_code == KeyCodes.S:
            player.vel.y = -vel_delta
        if key_code == KeyCodes.LEFT:
            overlay.vel.x = -cam_vel_delta
        if key_code == KeyCodes.RIGHT:
            overlay.vel.x = cam_vel_delta
        if key_code == KeyCodes.UP:
            overlay.vel.y = cam_vel_delta
        if key_code == KeyCodes.DOWN:
            overlay.vel.y = -cam_vel_delta
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
        if key_code == KeyCodes.LEFT:
            overlay.vel.x = 0
        if key_code == KeyCodes.RIGHT:
            overlay.vel.x = 0
        if key_code == KeyCodes.UP:
            overlay.vel.y = 0
        if key_code == KeyCodes.DOWN:
            overlay.vel.y = 0


if __name__ == "__main__":
    cog.init()
    player_id, block_ids, overlay_id = game_init()
    while not cog.hasquit():
        cog.loopstep()
        game_mainloop(player_id, block_ids, overlay_id)
    cog.quit()
