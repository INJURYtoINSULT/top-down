import libtcodpy as libtcod
 
#actual size of the window
SCREEN_WIDTH = 120
SCREEN_HEIGHT = 75
 
LIMIT_FPS = 20  #20 frames-per-second maximum

def draw_player():
    libtcod.console_put_char(0, 60, 37, '@', libtcod.BKGND_NONE)
    libtcod.console_put_char(0, 60, 36, 'I', libtcod.BKGND_NONE)

def draw_line(x0, y0, x1, y1):
    libtcod.line_init(x0, y0, x1, y1)
    x,y = x0,y0
    while (not x is None):
        libtcod.console_put_char(0, x, y, 'R', libtcod.red)
        x,y = libtcod.line_step()

def make_map():
    draw_player()
    draw_line(10, 10, 12, 12)
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_print(con, 10, 10, get_mouse_pos())    
    libtcod.console_flush()
           
def handle_keys():
#    global playerx, playery
 
    global key
 
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game

    else:
        return False
    #movement keys
#    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
#        playery -= 1
 
#    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
#        playery += 1
 
#    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
#        playerx -= 1
 
#    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
#        playerx += 1

def get_mouse_pos():
    global mouse
    (x,y) = (mouse.cx, mouse.cy)
    return str((x,y))

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD) 
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Ego', False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

key = libtcod.Key()
mouse = libtcod.Mouse()
while not libtcod.console_is_window_closed():
    libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS|libtcod.EVENT_MOUSE,key,mouse) 

    libtcod.console_set_default_foreground(0, libtcod.white)

    make_map()
    
    print get_mouse_pos()
 
    libtcod.console_flush()

    exit = handle_keys()
    if exit:
        break
